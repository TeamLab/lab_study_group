n =int(input())
ability = [list(map(int, input().split())) for i in range(n)]

from itertools import permutations
from itertools import combinations

case = (list(combinations([i for i in range(n)], n//2)))

diff=[]
for _ in range(len(case)//2):
    team =[]
    rival_team=[]
    for s,w in permutations(case[0],2):
        team.append(ability[s][w])
    for s,w in permutations(case[-1],2):
        rival_team.append(ability[s][w])
    diff.append(abs(sum(rival_team) - sum(team)))
    case.pop(0)
    case.pop()
min(diff)
