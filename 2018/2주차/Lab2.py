def boolean(matrix):
    i = 0
    row_boolean = [True] * N
    for row in matrix:
        stack = 1
        penalty = 0
        for n, m in zip(row[:-1], row[1:]) :    
            if abs(n-m) > 1 :
                row_boolean[i] = False
                break
            if n==m :
                stack += 1
            else :
                if m > n :
                    if stack - L - penalty < 0 :
                        row_boolean[i] = False
                        stack = 1
                        penalty = 0
                        break
                    stack = 1
                    penalty = 0
                else :
                    if stack - penalty < 0 :
                        row_boolean[i] = False
                        penalty = 0
                        stack = 1
                        break
                    penalty = L
                    stack = 1
        if stack - penalty < 0 :
            row_boolean[i] = False
        i += 1
    return row_boolean
N, L = map(int, input().split())
matrix = [[int(num) for num in input().split()] for _ in range(N)]
print(sum(boolean(matrix)+boolean(list(zip(*matrix)))))