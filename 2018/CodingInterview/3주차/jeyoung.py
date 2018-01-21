import sys
def circuit_queue(sub_rot, pop_i, matrix):
    if sub_rot == 1:
        row_matrix = matrix.pop(pop_i)
        row_matrix.insert(0, row_matrix.pop())
        matrix.insert(pop_i, row_matrix)
    elif sub_rot == -1:
        row_matrix = matrix.pop(pop_i)
        row_matrix.append(row_matrix.pop(0))
        matrix.insert(pop_i,row_matrix) 
    return matrix

def gear(matrix, step, n, direction):
    for i in range(step):
        bool_state = list(map(lambda x: True if x[0]!=x[1] else False, [[matrix[0][2],matrix[1][6]],
                                                                        [matrix[1][2],matrix[2][6]],
                                                                        [matrix[2][2],matrix[3][6]]]))
        
        tmp = direction[i]
        gear = n[i]-1
        for right_i in range(gear,3):
            if bool_state[right_i] == False: break 
            elif bool_state[right_i] == True:
                sub_rotation = -1*tmp
                circuit_queue(sub_rotation, right_i+1, matrix)
                tmp = sub_rotation        
        tmp = direction[i]        
        for left_i in range(gear-1,-1,-1):
            if bool_state[left_i] == False: break   
            elif bool_state[left_i] == True:
                sub_rotation = -1*tmp
                circuit_queue(sub_rotation, left_i, matrix)
                tmp = sub_rotation     
        circuit_queue(direction[i], gear, matrix) 
    sys.stdout.write(str(sum(list(map(lambda x: x[0]*x[1],list(zip([row[0] for row in matrix],[1,2,4,8]))))))) 
matrix = [list(map(lambda x: int(x), input().split())) for i in range(4)]
step = int(input())
n_direction = list(map(int, input().split()) for i in range(step))
n, direction = zip(*n_direction)
gear(matrix, step, n, direction)
