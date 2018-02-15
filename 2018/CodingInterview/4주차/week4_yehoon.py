from itertools import combinations

def get_team_list():
    n = int(input())
    all_player_ability = []
    for i in range(n):
        all_player_ability.append(list(map(int, input().split())))
    player_list = [i for i in range(n)]
    player_combi = list(combinations(player_list, int(len(player_list)/2)))
    start = player_combi[0:int(len(player_combi)/2)]
    link = player_combi[int(len(player_combi)/2):]
    link = link[::-1]
    team_list = list(zip(start, link))
    return team_list, all_player_ability

def summation(ability, player_idx):
    sum_list = []
    for i in player_idx:
        for j in player_idx
            sum_list.append(ability[i][j] + ability[j][i])
    return sum(set(sum_list))

def min_score(team_list):
    team_score = []
    for i in team_list:
        start, link = list(i)
        start_score = summation(all_player_ability, list(start))
        link_score = summation(all_player_ability, list(link))
        team_score.append(abs(start_score-link_score))
    result = min(set(team_score))
    return result

team_list, all_player_ability  = get_team_list()
min_score = min_score(team_list)
print(min_score)