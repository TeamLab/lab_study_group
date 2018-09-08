first = str(input())
first2 = list(first)

if first[2] != '*' and first[2] != '#':
    first2.insert(2, '')

if first[4] != '*' and first[4] != '#':
    first2.insert(5, '')

if len(first2) != 9:
        first2.append('')

if first2[1] != 'D' and first2[1] != 'S' and first2[1] != 'T':
    first2[0]=first2[0]+first2[1]
    del first2[1]

if first2[4] != 'D' and first2[4] != 'S' and first2[4] != 'T':
    first2[3]=first2[3]+first2[4]
    del first2[4]

if first2[7] != 'D' and first2[7] != 'S' and first2[7] != 'T':
    first2[6]=first2[6]+first2[7]
    del first2[7]

if len(first2) != 9:
        first2.append('')

# 1번째 기회 점수계산

if first2[1] == 'S':
    if first2[2] == '*':
        answer1 = (int(first2[0])**1)*2
    elif first2[2] == '#':
        answer1 = (int(first2[0])**1)*(-1)
    else:
        answer1 = int(first2[0])**1
elif first2[1] == 'D':
    if first2[2] == '*':
        answer1 = (int(first2[0])**2)*2
    elif first2[2] == '#':
        answer1 = (int(first2[0])**2)*(-1)
    else:
        answer1 = int(first2[0])**2
elif first2[1] == 'T':
    if first2[2] == '*':
        answer1 = (int(first2[0])**3)*2
    elif first2[2] == '#':
        answer1 = (int(first2[0])**3)*(-1)
    else:
        answer1 = int(first2[0])**3

# 2번째 기회 점수계산

if first2[4] == 'S':
    if first2[5] == '*':
        answer2 = (int(first2[3])**1)*2
        answer1 = answer1*2
    elif first2[5] == '#':
        answer2 = (int(first2[3])**1)*(-1)
    else:
        answer2 = int(first2[3])**1
elif first2[4] == 'D':
    if first2[5] == '*':
        answer2 = (int(first2[3])**2)*2
        answer1 = answer1*2
    elif first2[5] == '#':
        answer2 = (int(first2[3])**2)*(-1)
    else:
        answer2 = int(first2[3])**2
elif first2[4] == 'T':
    if first2[5] == '*':
        answer2 = (int(first2[3])**2)*3
        answer1 = answer1*2
    elif first2[5] == '#':
        answer2 = (int(first2[3])**3)*(-1)
    else:
        answer2 = int(first2[3])**3

# 3번째 기회 점수계산

if first2[7] == 'S':
    if first2[8] == '*':
        answer3 = (int(first2[6])**1)*2
        answer2 = answer2*2
    elif first2[8] == '#':
        answer3 = (int(first2[6])**1)*(-1)
    else:
        answer3 = int(first2[6])**1
elif first2[7] == 'D':
    if first2[8] == '*':
        answer3 = int(first2[6]**2)*2
        answer2 = answer2*2
    elif first2[8] == '#':
        answer3 = int(first2[6]**2)*(-1)
    else:
        answer3 = int(first2[6])**2
elif first2[7] == 'T':
    if first2[8] == '*':
        answer3 = (int(first2[6])**3)*2
        answer2 = answer2*2
    elif first2[8] == '#':
        answer3 = (int(first2[6])**3)*(-1)
    else:
        answer3 = int(first2[6])**3

final = answer1 + answer2 + answer3
print(final)