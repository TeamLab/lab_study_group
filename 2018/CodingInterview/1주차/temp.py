from itertools import product
from itertools import permutations

def get_max_min(n, numbers, arithmetics):
    return max(result), min(result)


# 6
# 1 2 3 4 5 6
# 2 1 1 1
n = 6
numbers = [1, 2, 3, 4, 5, 6]
arithmetics = [2, 1, 1, 1]


indexes = [[i, x] for i, x in enumerate(arithmetics) if x > 0]
print(indexes)
result = ""
for index, value in indexes:
    result += str(index)*value

from itertools import permutations
print(result)
a = set(["".join(x) for x in permutations(map(str, result))])
print(a)
result = []
for arithmetic in a:
    number_2 = numbers.copy()
    value = number_2.pop(0)
    arithmetic_2 = list(arithmetic)
    for i in range(n-1):
        ar = arithmetic_2.pop(0)
        if ar == "0":
            value = value + number_2.pop(0)
        elif ar =="1":
            value = value - number_2.pop(0)
        elif ar =="2":
            value = value * number_2.pop(0)
        elif ar =="3":
            if value < 0:
                value = abs(value)
                value = -(value // number_2.pop(0))
            else:
                value = value // number_2.pop(0)
    result.append(value)

print(max(results))
print(min(results))
