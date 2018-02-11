N, M, x, y, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
move = list(map(int, input().split()))
dice = [0, 0, 0, 0, 0, 0]
Upper_face = dice[0]
place = [x, y]
answer = list()
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def operate(a):

    if a == 1:
        if y != M - 1:
            error = dice[5]
            dice[5] = dice[3]
            dice[3] = dice[0]
            dice[0] = dice[2]
            dice[2] = error
            place[1] = y+1
        else:
            False

    elif a == 2:
        if y != 0:
            error = dice[5]
            dice[0] = dice[3]
            dice[2] = dice[0]
            dice[5] = dice[2]
            dice[3] = error
            place[1] = y-1
        else:
            False

    elif a == 3:
        if x != 0:
            error = dice[1]
            dice[1] = dice[5]
            dice[5] = dice[4]
            dice[4] = dice[0]
            dice[0] = error
            place[0] = x-1
        else:
            False

    elif a == 4:
        if x != N - 1:
            error = dice[1]
            dice[1] = dice[0]
            dice[0] = dice[4]
            dice[4] = dice[5]
            dice[5] = error
            place[0] = x+1
        else:
            False

if matrix[x][y] != 0:
    dice[5] = matrix[x][y]

elif matrix[x][y] == 0:
    matrix[x][y] = dice[5]

    for i in move:
        operate(i)
        x = place[0]
        y = place[1]
        if matrix[x][y] != 0:
            dice[5] = matrix[x][y]

        elif matrix[x][y] == 0:
            matrix[x][y] = dice[5]

        Upper_face = dice[0]
        answer.append(int(Upper_face))
print(answer)