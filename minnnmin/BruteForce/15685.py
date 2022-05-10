import sys, math
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
houses = []
chickens = []

for i in range(N):
    tmp = list(map(int, sys.stdin.readline().split()))
    for j, value in enumerate(tmp):
        if value == 1:
            houses.append((i+1, j+1))
        elif value == 2:
            chickens.append((i+1, j+1))
        else:
            continue

def dist(pos1, pos2):
    return abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1])

def myChickenDist(home, chicken):
    sum = 100
    for ch in chicken:
        if dist(home, ch) < sum:
            sum = dist(home, ch)
    return sum

def cityChickenDist(houses, chickens):
    sum = 0
    for h in houses:
        sum += myChickenDist(h, chickens)
    return sum

def minCityChickenDist():
    sum = math.inf
    for tmp_chickens in combinations(chickens, M):
        if cityChickenDist(houses, tmp_chickens) < sum:
            sum = cityChickenDist(houses, tmp_chickens)
    return sum

result = minCityChickenDist()
print(result)

# python을 c언어처럼 짜버렸네요