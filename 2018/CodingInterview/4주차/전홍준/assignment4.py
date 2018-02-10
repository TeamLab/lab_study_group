from itertools import combinations

number=int(input("4 이상 20 이하의 짝수를 입력하세요:"))

if 4 > number or number > 20 or number%2 != 0:
    print("숫자를 잘못 입력하였습니다.")
else:
    matrix = [[input() for col in range(number)] for row in range(number)]
    for i in range(number):
        matrix[i][i]=0
print(matrix)

min_value = float('inf')
for start in combinations(range(number), number//2):
    link = set(range(number)) - set(start)
    ability = 0
    for i in start:
        for j in start: ability+=int(matrix[i][j])
    for i in link:
        for j in link: ability-=int(matrix[i][j])
    min_value = min(min_value, abs(ability))
print("능력치 차이의 최소값:",min_value)