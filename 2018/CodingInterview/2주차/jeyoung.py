def slope_way(N,L,matrix):
    count = 0
    for row in matrix:
        hash_table = ["0"]*N
        for i in range(N-1):
            if abs(row[i]-row[i+1])>1:
                hash_table = [False]
            elif row[i] > row[i+1]:
                if i+L > N-1 or len(set(row[i+1:i+L+1]))!= 1:
                    hash_table = [False]
                if False not in hash_table[i+1:i+L]:
                    hash_table[i+1:i+L] = [True]*L
                    hash_table = hash_table[0:N]  
            elif row[i] < row[i+1]:
                if len(set(hash_table[i-L+1:i+1])) != 1 or i-L+1 <0 :
                    hash_table = [False]
                if True in hash_table[i-L+1:i+1]:
                    hash_table = [False]    
                if False not in hash_table[i-L+1:i+1]:
                    hash_table[i-L+1:i+1] = [True]*L    
        if False not in hash_table :             
             count += 1   
    return count
N, L = map(int, input().split())
matrix = [list(map(int, input().split())) for i in range(N)]
result = slope_way(N,L,matrix) + slope_way(N,L,zip(*matrix))
