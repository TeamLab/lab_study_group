def input_values():
    n = int(input())
    numbers = list(map(int, input().split()))
    arithmetics = list(map(int, input().split()))

    return n, numbers, arithmetics

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return int(a / b)

def generate_operators_list(arithmetics):
    operators = {0: "add ", 1: "sub ", 2: "mul ", 3: "div "}
    operators_str = ""
    for idx in range(len(arithmetics)):
        if arithmetics[idx] != 0:
            operators_str += operators[idx] * arithmetics[idx]

    from itertools import permutations

    operators_permutation = permutations(operators_str.strip().split(" "), len(operators_str.strip().split(" ")))
    set_permutation = list(set(operators_permutation))

    return set_permutation

def get_values(numbers, set_permutation):
    operator_func = {"add": add, "sub": sub, "mul": mul, "div": div}
    result_of_operations = []

    for idx_1 in range(len(set_permutation)):
        result_list = []
        result_list.append(numbers[0])
        for idx_2 in range(len(set_permutation[idx_1])):
            operator_idx = set_permutation[idx_1][idx_2]
            result_list.append(operator_func[operator_idx](result_list[idx_2], numbers[idx_2 + 1]))
        result_of_operations.append(result_list[-1])
    return result_of_operations

def get_max_min(result_list):
    return max(result_list), min(result_list)

n, numbers, arithmetics = input_values()
set_permutation = generate_operators_list(arithmetics)
result_list = get_values(numbers, set_permutation)
result_max, result_min = get_max_min(result_list)

print(result_max, result_min)