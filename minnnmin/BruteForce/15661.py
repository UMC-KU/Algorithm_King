import sys, math
from itertools import combinations

N = int(input())
ability_list = {i: [] for i in range(1, N+1)}

for i in range(1, N+1):
    tmp = [i for i in map(int, sys.stdin.readline().split())]
    ability_list[i] = tmp

# ability_list = {1: [0, 1, 2, 3], 2: [4, 0, 5, 6], 3: [7, 1, 0, 2], 4: [3, 4, 5, 0]}

# 어느 팀의 ability
def abilityOfTeam(team_list):
    ability = 0
    for i, member in enumerate(team_list):
        for member2 in team_list[i+1:]:
            ability += ability_list[member][member2-1] + ability_list[member2][member-1]
    return ability

# 두팀 능력치 차이
def gap(team1, team2):
    return abs(abilityOfTeam(team1) - abilityOfTeam(team2))

def anotherTeamOf(teamA):
    teamB = []
    for i in range(1, N+1):
        if i in teamA:
            continue
        else:
            teamB.append(i)
    return tuple(teamB)

result = math.inf # 두 팀의 능력치 차의 최솟값

for n in range(N//2, 0, -1): # n = N//2  N//2-1  N//2-2  ...  1
    # 한 팀이 n명일 때 그 게임의 팀 갭 차이
    tmp_sum = math.inf
    for teamA in combinations(range(1, N+1), n): #teamA에 n명 배정
        teamB = anotherTeamOf(teamA)
        if gap(teamA, teamB) < tmp_sum:
            tmp_sum = gap(teamA, teamB)
    if tmp_sum < result:
        result = tmp_sum

print(result)

# pypy로 돌리면 간신히 통과한다. 무려 2분이나 걸리지만