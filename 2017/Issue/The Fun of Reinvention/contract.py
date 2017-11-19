_contracts = {}


class Contract:
    @classmethod
    def __init_subclass__(cls):
        _contracts[cls.__name__] = cls

    def __set__(self, instance, value):
        self.check(value)
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name

    @classmethod
    def check(cls, value):
        pass


class Typed(Contract):
    @classmethod
    def check(cls, value):
        assert isinstance(value, cls.type), f'Expected {cls.type}'
        # f'a = {a}' 은 PEP 498의 F-String 이라는 문법
        super().check(value)
        i = 1


class Integer(Typed):
    type = int


class Float(Typed):
    type = float


class String(Typed):
    type = str


class Positive(Contract):
    @classmethod
    def check(cls, value):
        assert value > 0, 'Must be > 0'
        super().check(value)


class PositiveInteger(Integer, Positive):
    pass


class NonEmpty(Contract):
    # 길이가 0보다 큰지 검사
    @classmethod
    def check(cls, value):
        assert len(value) > 0, 'Must be nonempty'
        super().check(value)


class NonEmptyString(String, NonEmpty):
    # 길이가 0보다 큰 문자열인지 검사
    pass


from functools import wraps
from inspect import signature


def checked(func):
    sig = signature(func)
    ann = ChainMap(
        func.__annotations__,
        func.__globals__.get('__annotations__'), {}
    )

    @wraps(func)
    # @wraps를 사용하는 이유:
    # 데코레이터 내부에서 인자로 전달받은 함수가 익명함수 처럼 취급되어 버리므로
    # 디버깅이 난해해지는 단점이 있었기 때문
    def wrapper(*args, **kwargs):
        bound = sig.bind(*args, **kwargs)
        for name, val in bound.arguments.items():
            if name in ann:
                ann[name].check(val)
        return func(*args, **kwargs)
    return wrapper


from collections import ChainMap


class BaseMeta(type):
    def __prepare__(cls, *args):
        return ChainMap({}, _contracts)

    def __new__(meta, name, bases, methods):
        methods = methods.maps[0]
        return super().__new__(meta, name, bases, methods)


class Base(metaclass=BaseMeta):
    @classmethod
    def __init_subclass__(cls):
        for name, val in cls.__dict__.items():
            if callable(val):
                setattr(cls, name, checked(val))

        for name, val in cls.__annotations__.items():
            contract = val()
            contract.__set_name__(cls, name)
            setattr(cls, name, contract)

    def __init__(self, *args):
        ann = self.__annotations__
        assert len(ann) == len(args), f'Expected {len(ann)} arguments'
        for name, val in zip(ann, args):
            setattr(self, name, val)

    def __repr__(self):
        args = ', '.join(repr(getattr(self, name)) for name in self.__annotations__)
        return f'{type(self).__name__}({args})'
