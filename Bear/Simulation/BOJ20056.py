import sys

N,M,K = map(int,sys.stdin.readline().rstrip().split())

dx = [0,1,1,1,0,-1,-1,-1]
dy = [-1,-1,0,1,1,1,0,-1]

fire = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    y,x,m,s,d =  map(int,sys.stdin.readline().rstrip().split())
    fire[y-1][x-1].append([m,s,d])

for _ in range(K):
    temp = [[[] for _ in range(N)] for _ in range(N)]

    for y in range(N):
        for x in range(N):
            if len(fire[y][x]):
                for i in range(len(fire[y][x])):
                    m = fire[y][x][i][0]
                    s = fire[y][x][i][1]
                    d = fire[y][x][i][2]

                    ny = (y + dy[d] * s) % N 
                    nx = (x + dx[d] * s) % N

                    temp[ny][nx].append([m,s,d])

    for y in range(N):
        for x in range(N):
            if len(temp[y][x]) >= 2:
                sum_m = 0
                sum_s = 0
                check_odd = True
                check_even = True
                num_fire = len(temp[y][x])
                for i in range(num_fire):
                    m = temp[y][x][i][0]
                    s = temp[y][x][i][1]
                    d = temp[y][x][i][2]

                    if d % 2 == 0:
                        check_odd == False
                    elif d % 2 == 1:
                        check_even == False
                    
                    sum_m += m
                    sum_s += s
                temp[y][x] = []
                m = sum_m // 5
                s = sum_s // num_fire

                for i in range(4):
                    if m != 0:
                        if check_even or check_odd:
                            temp[y][x].append([m,s,i*2])
                        else:
                            temp[y][x].append([m,s,i*2+1])
                    else:
                        continue
                    
                
                    
    fire = temp

answer = 0

for y in range(N):
    for x in range(N):
        for i in range(len(fire[y][x])):
            answer += fire[y][x][i][0]

print(answer)        

                

        



            


