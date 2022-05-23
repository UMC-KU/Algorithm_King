import sys
from collections import deque

sharkX = 0
sharkY = 0
sharkSize=2

dx = [0,0,1,-1]
dy = [1,-1,0,0]

N = int(sys.stdin.readline().rstrip())
sea = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

for y in range(N):
    for x in range(N):
        if sea[y][x] == 9:
            sharkX, sharkY = x,y

sea[sharkY][sharkX]=0

def bfs(sharkY,sharkX,sharkSize):
    q= deque()
    q.append((sharkY,sharkX,0))
    visited = [[False]*N for _ in range(N)]
    visited[sharkY][sharkX] = True
    fish = []
    while len(q) > 0:
        y,x,dist = q.popleft()        

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if nx>=0 and nx<N and ny>=0 and ny<N and not visited[ny][nx]:
                if sea[ny][nx] <= sharkSize: # 상어가 갈 수 있는 길이면,
                    visited[ny][nx] = True
                    if 0 < sea[ny][nx] and sea[ny][nx] < sharkSize: #물고기
                        q.append((ny,nx,dist+1))
                        fish.append((dist+1,ny,nx))
                    elif sea[ny][nx] == 0 or sea[ny][nx] == sharkSize: #물고기 아님
                        q.append((ny,nx,dist+1))
    
    fish.sort()
    if len(fish) != 0:
        return fish[0]
    else:
        return []

answer = 0
eat = 0

while True:
    fish_eat = bfs(sharkY, sharkX,sharkSize) # 가장 가까운 거리에 있는 물고기 먹은거
    if len(fish_eat) != 0:
        dist,y,x = fish_eat
        
        sea[y][x] = 0
        eat += 1
        answer += dist
        if eat == sharkSize:
            sharkSize += 1
            eat = 0
        sharkY, sharkX = y, x
    else:
        break

print(answer)




