A = [1, 0, 1, 0, 1, 1, 1, 1]
B = [0, 1, 1, 1, 1, 1, 0, 1]
C = [1, 1, 0, 0, 1, 1, 1, 0]
D = [0, 0, 0, 0, 0, 0, 1, 0]
index_list = [0] * 4
a, b, c, d = index_list
cal_case_1 = [lambda x : x-1, lambda x : x+1, lambda x : x-1, lambda x : x+1]
cal_case_2 = [lambda x : x+1, lambda x : x-1, lambda x : x+1, lambda x : x-1]




n = 3
t = -1

bool_list = [A[a+2%8] != B[b+6%8], B[b+2%8] != C[c+6%8], C[c+2%8] != D[d+6%8]]

a = [0]
i = 0
for bo in bool_list:
    if not bo:
        i += 1
    a.append(i)
    
if n*t in [1, -2, 3, -4] :
    for i, b in enumerate(a) :
        if b == a[n-1] :
            index_list[b] = cal_case_1[b](index_list[b])
else :
    for i, b in enumerate(a) :
        if b == a[n-1] :
            index_list[b] = cal_case_2[b](index_list[b])
a, b, c, d = index_list

print(A[a%8] + B[b%8]*2 + C[c%8]*4 + D[d%8]*8)