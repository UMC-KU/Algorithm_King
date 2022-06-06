import sys


#R행 C열 T초 후
R,C,T = map(int,sys.stdin.readline().rstrip().split())
room = []

dr = [0,0,1,-1]
dc = [1,-1,0,0]

for _ in range(R):
    room.append(list(map(int,sys.stdin.readline().rstrip().split())))


for _ in range(T):
    # 확산
    temp_room = [list(0 for a in range(C)) for b in range(R)]

    for r in range(R):
        for c in range(C):
            spread = room[r][c] // 5
            sum = 0
            if spread > 0:
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if nr >= 0 and nr < R and nc >= 0 and nc < C:
                        if room[nr][nc] != -1:
                            temp_room[nr][nc] += spread
                            sum += 1
            temp_room[r][c] += (room[r][c] - spread*sum)

    #print(temp_room)    

    temp_room2 = [list(0 for a in range(C)) for b in range(R)]

    check = False
    for r in range(R):
        if room[r][0] == -1:
            #위쪽
            temp_room2[r][0] = -1
            if not check:
                check = True
                for x in range(1,C-1):
                    temp_room2[r][x+1] = temp_room[r][x]
                for y in range(r-1,-1,-1):
                    temp_room2[y][C-1] = temp_room[y+1][C-1]
                for x in range(C-2,-1,-1):
                    temp_room2[0][x] = temp_room[0][x+1]
                for y in range(1,r):
                    temp_room2[y][0] = temp_room[y-1][0]
            else:
                for x in range(1,C-1):
                    temp_room2[r][x+1] = temp_room[r][x]
                for y in range(r+1,R):
                    temp_room2[y][C-1] = temp_room[y-1][C-1]
                for x in range(C-2,-1,-1):
                    temp_room2[R-1][x] = temp_room[R-1][x+1]
                for y in range(R-2,r,-1):
                    temp_room2[y][0] = temp_room[y+1][0]
        else:
            if r > 0 and r < R-1:
                for x in range(1,C-1):
                    temp_room2[r][x] = temp_room[r][x]
    room = temp_room2


answer = 0

for r in range(R):
    for c in range(C):
        if room[r][c] !=-1:
            answer += room[r][c]

    

print(answer)