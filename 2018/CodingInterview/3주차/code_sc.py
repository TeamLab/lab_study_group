
# input_data = """
# 10101111
# 01111101
# 11001110
# 00000010
# 2
# 3 -1
# 1 1
# """
# matrix_data = input_data.strip().split("\n")[:4]
#
# n_direction_data = input_data.strip().split("\n")[5:]
#
# matrix = [deque(list(line)) for line in matrix_data]
# step = int(input_data.strip().split("\n")[4])
# n, direction = zip(*[list(map(int, line.split(" "))) for line in n_direction_data])

from collections import deque
matrix = []
matrix.append(deque([int(i) for i in input()]))
matrix.append(deque([int(i) for i in input()]))
matrix.append(deque([int(i) for i in input()]))
matrix.append(deque([int(i) for i in input()]))
step = int(input())
n = []
direction = []
for _ in range(step):
    w, t = list(map(int, input().split()))
    n.append(w)
    direction.append(t)

for i in range(step):
    change_list = [0, 0, 0, 0]
    target_gear = n[i]-1
    left_gear_index = list(range(0, target_gear))[::-1]
    right_gear_index = list(range(target_gear+1, 4))

    direction_value = direction[i]
    change_list[target_gear] = direction_value

    for l_i in left_gear_index:
        if matrix[l_i][2] == matrix[target_gear][6]:
            break
        if matrix[l_i][2] != matrix[target_gear][6]:
            direction_value = -direction_value
            target_gear = l_i
            change_list[target_gear] = direction_value

    direction_value = direction[i]
    for r_i in right_gear_index:
        if matrix[r_i][6] == matrix[target_gear][2]:
            break
        if matrix[r_i][6] != matrix[target_gear][2]:
            direction_value = -direction_value
            target_gear = r_i
            change_list[target_gear] = direction_value

    for index, line in zip(change_list, matrix):
        line.rotate(index)

result = 0
for i, line in enumerate(matrix):
    result += int(line[0]) * (2**(i))
print(result)
