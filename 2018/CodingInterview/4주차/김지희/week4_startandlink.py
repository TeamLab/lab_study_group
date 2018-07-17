
# coding: utf-8




from itertools import permutations
from itertools import combinations





member= int(input())
score_list =  [list(map(int, input().split())) for i in range(member)]



comb_of_member = list(combinations([i for i in range(member)],member//2))
res = (list(zip(comb_of_member, comb_of_member[::-1])))
result_list =[]
for comb  in res:
    start, link = comb
    total_score_start = 0
    total_score_link = 0
    start2pack = list(permutations(start,2))
    link2pack = list(permutations(link,2))
    for i in range(len(start2pack)):
        first_s, second_s = start2pack[i]
        total_score_start += score_list[first_s][second_s]
        first_l, second_l = link2pack[i]
        total_score_link += score_list[first_l][second_l]
    result_list.append(abs(total_score_link-total_score_start))
print(min(result_list))    







