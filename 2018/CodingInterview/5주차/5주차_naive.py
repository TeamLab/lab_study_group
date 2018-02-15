from itertools import combinations
import copy

def infection(mat) :
    safety = unsafe(mat)
    while safety :
        for n, row in enumerate(mat) :
            if row.count(2) :
                for z in [i for i, v in enumerate(row) if v == 2] :
                    for k in range(z, len(row)) :
                        if row[k] == 1 :
                            break
                        mat[n][k] = 2
                    for k in range(z, 0, -1) :
                        if row[k-1] == 1 :
                            break
                        mat[n][k-1] = 2
        for n, col in enumerate(zip(*mat)) :
            if col.count(2) :
                for z in [i for i, v in enumerate(col) if v == 2] :
                    for k in range(z, len(col)) :
                        if col[k] == 1 :
                            break
                        mat[k][n] = 2
                    for k in range(z, 0, -1) :
                        if col[k-1] == 1 :
                            break
                        mat[k-1][n] = 2
        safety = unsafe(mat)
    return mat

def unsafe(mat) :
    for row in mat :
        for i in range(len(row)-1) :
            if row[i] == 0 :
                if row[i+1] == 2 :
                    return True
            if row[i] == 2 :
                if row[i+1] == 0 :
                    return True
    for col in zip(*mat) :
        for j in range(len(col)-1) :
            if col[j] == 0 :
                if col[j+1] == 2 :
                    return True
            if col[j] == 2 :
                if col[j+1] == 0 :
                    return True
    return False

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]

zeros = []
clean = 0

for i, list in enumerate(lab) :
    for j, num in enumerate(list) :
        if num == 0 :
            zeros.append([i, j])
for zero in combinations(zeros, 3) :
    lab_temp = copy.deepcopy(lab)
    for index in zero :
        i, j = index
        lab_temp[i][j] = 1
    infection(lab_temp)
    if clean < sum([row.count(0) for row in lab_temp]) :
        clean = sum([row.count(0) for row in lab_temp])
print(clean)