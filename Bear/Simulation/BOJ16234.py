from collections import deque
import sys


#R행 C열 T초 후
N,L,R = map(int,sys.stdin.readline().rstrip().split())

country = []
visited = []

dy = [0,0,1,-1]
dx = [1,-1,0,0]

for _ in range(N):
    country.append(list(map(int,sys.stdin.readline().rstrip().split())))


def bfs(r,c):
    q = deque()
    q.append([r,c])
    team = []
    team.append([r,c])

    while len(q) != 0:
        y,x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < N and ny >= 0 and ny < N and not visited[ny][nx]:
                if L <= abs(country[ny][nx] - country[y][x]) and abs(country[ny][nx] - country[y][x]) <= R:
                    visited[ny][nx] = True
                    q.append([ny,nx])
                    team.append([ny,nx])
    
    return team



answer = 0

while True:
    visited = [[False] * (N) for _ in range(N)]
    check = True
    for r in range(N):
        for c in range(N):
            
            if visited[r][c] == False:
                visited[r][c] = True
                t = bfs(r,c)
                

                if len(t) > 1:
                    check = False
                    s = 0
                    for y,x in t:
                        s += country[y][x]
                    for y,x in t:
                        country[y][x] = s // len(t)
                   
                        
    if check:
        break
    answer+=1

print(answer)

