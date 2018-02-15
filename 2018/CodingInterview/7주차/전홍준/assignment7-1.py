n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

answer = []
answer2 = []
answer3 = []
answer4 = []
final = [['0' for col in range(n)] for row in range(n)]
treasure = ['0' for col in range(n)]

for i in arr1:
    answer.append(bin(i)[2:])

for i in range(5):
    answer2.append(list(answer[i]))

for i in range(5):
    while len(answer2[i]) != n:
        answer2[i].insert(0, '0')

for i in arr2:
    answer3.append(bin(i)[2:])

for i in range(5):
    answer4.append(list(answer3[i]))

for i in range(5):
    while len(answer4[i]) != n:
        answer4[i].insert(0, '0')

for i in range(n):
    for j in range(n):
        if answer2[i][j] == '1' or answer4[i][j] == '1':
            final[i][j] = '#'
        else:
            final[i][j] = ''

for i in range(5):
    treasure[i] = ' '.join(final[i])

print(treasure)
