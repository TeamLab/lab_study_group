# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 01:16:38 2018
@author: Jin
"""
import itertools


### 오류 정의 ###
class LengthError(Exception):
    def __str__(self):
        return '입력된 파라미터의 길이가 알맞지 않습니다.'


### 사칙연산 함수 정의 ###
def add(a, b):
    return a + b


def minus(a, b):
    return a - b


def product(a, b):
    return a * b


def div(a, b):
    if a < 0:
        return -(abs(a) // b)
    return a // b


### 주어진 연산자로 가능한 연산 조합 만들기 ###
def bundle(arithmetics):
    arith_list = []
    arith_dict = {0: add, 1: minus, 2: product, 3: div}
    idx = 0
    for num in arithmetics:
        for _ in range(num):
            arith_list.append(arith_dict[idx])
        idx += 1
    return list(set([tup for tup in itertools.permutations(arith_list, sum(arithmetics))]))
    # 이 부분은 list comprehension으로 간단하게 만들 수 있을지 다시 코드 짜보기


### 연산자 조합과 숫자를 이용하여 계산하기 ###
def cal(number, arithmetic):
    idx = 0
    for _ in range(len(arithmetic)):
        if idx == 0:
            result = arithmetic[idx](number[idx], number[idx + 1])
        else:
            result = arithmetic[idx](result, number[idx + 1])
        idx += 1
    return result


### 연산되는 결과들 리스트로 받아오기 ###
def makelist(numbers, arithmetics):
    arith_list = bundle(arithmetics)
    result = []
    for arithmetic in arith_list:
        result.append(cal(numbers, arithmetic))
    return result


### 최대값 최소값 찾아서 반환하기 ###
def get_max_min(arith_list):
    return max(arith_list), min(arith_list)


### 메인함수 정의 ###
def main():
    n = int(input())
    numbers = list(map(int, input().split()))
    arithmetics = list(map(int, input().split()))
    if len(numbers) != n:
        print(numbers, n, '첫 번째 길이 오류')
        raise LengthError
    if len(numbers) - 1 != sum(arithmetics):
        print(len(numbers) - 1, sum(arithmetics), '두 번째 길이 오류')
        raise LengthError
    if len(numbers) < 2 or len(numbers) > 11:
        print(len(numbers), '세 번째 길이 오류')
        raise LengthError
    print(get_max_min(makelist(numbers, arithmetics))[0])
    print(get_max_min(makelist(numbers, arithmetics))[1])
main()