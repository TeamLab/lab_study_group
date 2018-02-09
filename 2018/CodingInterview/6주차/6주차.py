n, m, x, y, k = map(int, input().split())
dice = [0]*6
loc = [x, y]
mat = [list(map(int, input().split())) for _ in range(n)]
def west() :
    temp = dice[5]
    dice[5] = dice[2]
    dice[2] = dice[0]
    dice[0] = dice[3]
    dice[3] = temp
    loc[1] -= 1
    
def east() :
    temp = dice[5]
    dice[5] = dice[3]
    dice[3] = dice[0]
    dice[0] = dice[2]
    dice[2] = temp
    loc[1] += 1

def north() :
    temp = dice[1]
    dice[1] = dice[5]
    dice[5] = dice[4]
    dice[4] = dice[0]
    dice[0] = temp
    loc[0] -= 1

def south() :
    temp = dice[1]
    dice[1] = dice[0]
    dice[0] = dice[4]
    dice[4] = dice[5]
    dice[5] = temp
    loc[0] += 1

roll = [east, west, north, south]
unroll = [west, east, south, north]
for o in map(int, input().split()) :
    try :
        roll[o-1]()
        x, y = loc
        if x < 0 or y < 0 :
            raise ValueError
        if mat[x][y] :
            dice[0] = mat[x][y]
            mat[x][y] = 0
        else :
            mat[x][y] = dice[0]
        print(dice[5])
    except :
        unroll[o-1]()
        continue