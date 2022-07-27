from itertools import combinations, permutations
from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def bfs(now_pos):
    q = deque()
    visited = [[False] * N for _ in range(N)]
    q.append(now_pos)
    visited[now_pos[0]][now_pos[1]] = True
    # print(now_pos)
    while q:
        pos = q.popleft()
        if arr[pos[0]][pos[1]] == 2:
            # print(pos[0], pos[1])
            # print(abs(pos[0] - now_pos[0]) + abs(pos[1] - now_pos[1]))
            return abs(pos[0] - now_pos[0]) + abs(pos[1] - now_pos[1])
        for i in range(4):
            ny = pos[0] + dy[i]
            nx = pos[1] + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if not visited[ny][nx]:
                    q.append((ny, nx))
                    visited[ny][nx] = True
                    if arr[ny][nx] == 2:
                        return abs(ny - now_pos[0]) + abs(nx - now_pos[1])


def backtracking(depth, cnt):
    global answer
    if cnt == len(chicken_pos) - M:
        # print(arr)
        sum = 0
        for i in range(len(house_pos)):
            if answer < sum:
                break
            sum += bfs(house_pos[i])
            # print(sum)
        answer = min(answer, sum)
        # print(answer)
        return
    for i in range(depth, len(chicken_pos)):
        if arr[chicken_pos[i][0]][chicken_pos[i][1]] == 2:
            # print(i)
            # check[i] = False
            arr[chicken_pos[i][0]][chicken_pos[i][1]] = 0
            backtracking(i, cnt + 1)
            # check[i] = True
            arr[chicken_pos[i][0]][chicken_pos[i][1]] = 2


# 0 0 0 0 0 0 0 0 0 2
N, M = map(int, input().rstrip().split())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().rstrip().split())))

house_pos = []
chicken_pos = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            house_pos.append((i, j))
        if arr[i][j] == 2:
            chicken_pos.append((i, j))
# check = [True] * chicken_house

answer = 1e9
backtracking(0, 0)

# for i in list(combinations(chicken_pos, chicken_house - M)):
#     # print(i)
#     for j in i:
#         arr[j[0]][j[1]] = 0
#     complement = list(set(chicken_pos) - set(i))
#     # print(complement)
#     backtracking(0, 0)
#     for j in i:
#         arr[j[0]][j[1]] = 2

print(answer)
