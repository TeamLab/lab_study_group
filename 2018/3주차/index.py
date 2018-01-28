A = [int(i) for i in input()]
B = [int(i) for i in input()]
C = [int(i) for i in input()]
D = [int(i) for i in input()]
n = int(input())
W = []
T = []
for _ in range(n) :
    w, t = list(map(int, input().split()))
    W.append(w)
    T.append(t)
index_list = [0] * 4
a, b, c, d = index_list
cal_case_1 = [lambda x : x-1, lambda x : x+1, lambda x : x-1, lambda x : x+1]
cal_case_2 = [lambda x : x+1, lambda x : x-1, lambda x : x+1, lambda x : x-1]

for w, t in zip(W, T) :
    bool_list = [A[a+2%8] != B[b+6%8], B[b+2%8] != C[c+6%8], C[c+2%8] != D[d+6%8]
    G = [0]
    i = 0
    for bo in bool_list :
        if not bo:
            i += 1
        G.append(i)
    
    if w*t in [1, -2, 3, -4] :
        for j, g in enumerate(G) :
            if g == G[w-1] :
                index_list[j] = cal_case_1[j](index_list[j])
    else :
        for j, g in enumerate(G) :
            if g == G[w-1] :
                index_list[j] = cal_case_2[j](index_list[j])
    a, b, c, d = index_list
print(A[a%8] + B[b%8]*2 + C[c%8]*4 + D[d%8]*8)
