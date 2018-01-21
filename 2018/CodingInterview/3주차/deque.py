import collections
A = collections.deque([int(i) for i in input()])
B = collections.deque([int(i) for i in input()])
C = collections.deque([int(i) for i in input()])
D = collections.deque([int(i) for i in input()])
k = int(input())
W = []
T = []
for _ in range(k) :
    w, t = list(map(int, input().split()))
    W.append(w)
    T.append(t)
for w, t in zip(W, T) :
    bool_list = [A[2] != B[6], B[2] != C[6], C[2] != D[6]]
    i=0
    group = [0]
    for bo in bool_list :
            if not bo:
                i += 1
            group.append(i)
    if w*t in [1, -2, 3, -4] :
        for n, g in enumerate(group) :
            if g == group[w-1] :
                if n == 0 :
                    A.rotate(1)
                elif n == 1 :
                    B.rotate(-1)
                elif n == 2 :
                    C.rotate(1)
                else :
                    D.rotate(-1)
    else :
        for n, g in enumerate(group) :
            if g == group[w-1] :
                if n == 0 :
                    A.rotate(-1)
                elif n == 1 :
                    B.rotate(1)
                elif n == 2 :
                    C.rotate(-1)
                else :
                    D.rotate(1)
        

print(A[0] + B[0]*2 + C[0]*4 + D[0]*8)