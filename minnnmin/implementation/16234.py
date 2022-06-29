import sys
from collections import deque

N, L, R = map(int, sys.stdin.readline().split())
countries = []
for _ in range(N):
    countries.append(list(map(int, sys.stdin.readline().split())))

def bfs(start_r, start_c):
    global changed, visited
    open_countries = [(start_r, start_c)] # 국경선 열린 나라들 좌표
    population = countries[start_r][start_c]
    q = deque([(start_r, start_c)])
    visited[start_r][start_c] = True
    while q: # 인접 좌표 검사 (상하좌우)
        r, c = q.popleft()
        if r - 1 >= 0 and not visited[r - 1][c]:
            if L <= abs(countries[r][c] - countries[r - 1][c]) <= R:
                open_countries.append((r - 1, c))
                population += countries[r - 1][c]
                q.append((r - 1, c))
                visited[r - 1][c] = True
        if r + 1 < N and not visited[r + 1][c]:
            if L <= abs(countries[r][c] - countries[r + 1][c]) <= R:
                open_countries.append((r + 1, c))
                population += countries[r + 1][c]
                q.append((r + 1, c))
                visited[r + 1][c] = True
        if c - 1 >= 0 and not visited[r][c - 1]:
            if L <= abs(countries[r][c] - countries[r][c - 1]) <= R:
                open_countries.append((r, c - 1))
                population += countries[r][c - 1]
                q.append((r, c - 1))
                visited[r][c - 1] = True
        if c + 1 < N and not visited[r][c + 1]:
            if L <= abs(countries[r][c] - countries[r][c + 1]) <= R:
                open_countries.append((r, c + 1))
                population += countries[r][c + 1]
                q.append((r, c + 1))
                visited[r][c + 1] = True

    if len(open_countries) >= 2:
        changed = True
        mix(open_countries, population)

def mix(open_countries, population):
    global countries
    new_population = population // len(open_countries)
    for country in open_countries:
        countries[country[0]][country[1]] = new_population

# 모든 점에 대해 BFS 수행
day = 0
changed = True
while changed:
    changed = False
    visited = []
    for _ in range(N):
        visited.append(list([False] * N))
    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                bfs(r, c)
    if changed:
        day += 1
print(day)