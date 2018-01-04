import itertools
def ad(a, b):
    return a + b
def m(a, b):
    return a - b
def p(a, b):
    return a * b
def d(a, b):
    if a < 0:
        return -(abs(a) // b)
    return a // b
def bundle(arithmetics):
    arith_list = []
    arith_dict = {0: ad, 1: m, 2: p, 3: d}
    idx = 0
    for num in arithmetics:
        for _ in range(num):
            arith_list.append(arith_dict[idx])
        idx += 1
    return list(set([tup for tup in itertools.permutations(arith_list, sum(arithmetics))]))
def cal(number, arithmetic):
    idx = 0
    for _ in range(len(arithmetic)):
        if idx == 0:
            result = arithmetic[idx](number[idx], number[idx + 1])
        else:
            result = arithmetic[idx](result, number[idx + 1])
        idx += 1
    return result

def makelist(numbers, arithmetics):
    arith_list = bundle(arithmetics)
    result = [cal(numbers, arithmetic) for arithmetic in arith_list]
    return result
def get_max_min(arith_list):
    return max(arith_list), min(arith_list)
def main():
    n = int(input())
    numbers = list(map(int, input().split()))
    arithmetics = list(map(int, input().split()))
    print(get_max_min(makelist(numbers, arithmetics))[0])
    print(get_max_min(makelist(numbers, arithmetics))[1])
main()