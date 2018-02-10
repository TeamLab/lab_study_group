from itertools import combinations
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
result = []
for i in combinations(range(n), int(n/2)) :
    start_score = 0
    link_score = 0
    link = set(range(n)) - set(i)
    for j, k in zip(combinations(i, 2), combinations(link, 2)):
        start_score += matrix[j[0]][j[1]]+matrix[j[1]][j[0]]
        link_score += matrix[k[0]][k[1]]+matrix[k[1]][k[0]]
    result.append(int(abs(start_score-link_score)))
print(min(result))
