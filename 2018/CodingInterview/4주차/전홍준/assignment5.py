from itertools import product

def operate(a1, b1, a2, b2, a3, b3):
    for i in range(0, N):
        for j in range(0, M):
            virus[i][j] = matrix[i][j]
            virus[a1][b1] = virus[a2][b2] = virus[a3][b3] = 1
            visited[i][j] = False
    for i in range(0, N):
        for j in range(0, M):
            if virus[i][j] == 2 and visited[i][j] == False:
                infection(i, j)
    safe = 0
    for i in range(0, N):
        for j in range(0, M):
            if virus[i][j] == 0:
                safe += 1
    return safe

def infection(i, j):
    if visited[i][j] == True:
        pass
    visited[i][j] =True
    virus[i][j] = 2
    for k in range(4):
        a = i+dx[k]
        b = j+dy[k]
        if a >= 0 and a < N and b >= 0 and b < M and virus[a][b] == 0:
            infection(a, b)

def check(a1, b1, a2, b2, a3, b3):
    if (matrix[a1][b1] == 1 or matrix[a1][b1] == 2 or matrix[a2][b2] == 1
        or matrix[a2][b2] == 2 or matrix[a3][b3] == 1 or matrix[a3][b3] == 2):
        return False
    if (a1 == a2 and b1 == b2) or (a1 == a3 and b1 == b3) or (a2 == a3 and b2 == b3):
        return False
    else:
        return True

N, M = map(int, input().split())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
matrix = [list(map(int, input().split())) for _ in range(N)]
virus = [[0 for col in range(M)] for row in range(N)]
visited = [[False for col in range(M)] for row in range(N)]

secure = 0
a=list()
for i in range(N):
    for j in range(M):
        a.append([i,j])
permutation = list(product(a,repeat=3))
for i, j, k in permutation:
    a1=i[0]
    b1=i[1]
    a2=j[0]
    b2=j[1]
    a3=k[0]
    b3=k[1]
    if check(a1, b1, a2, b2, a3, b3)==True:
        secure = max(secure, operate(a1, b1, a2, b2, a3, b3))
print(secure)