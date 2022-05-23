import sys

N,M = map(int,sys.stdin.readline().rstrip().split())

A = []
Cloud = [(N-1,0),(N-1,1),(N-2,0),(N-2,1)]
dy8 = (0, -1, -1, -1, 0, 1, 1, 1)
dx8 = (-1, -1, 0, 1, 1, 1, 0, -1)
dy4 = (-1, -1,  1, 1)
dx4 = (-1,  1, -1, 1)


for i in range(N):
    A.append(list(map(int,sys.stdin.readline().rstrip().split())))
    

move =[]

for i in range(M):
    move.append(list(map(int,sys.stdin.readline().rstrip().split())))

for d,s in move:

    temp = []
    d-=1
    visited = []
    for i in range(N):
        visited.append(list(False for _ in range(N)))

    for y,x in Cloud:
        	
        ny = (y + dy8[d] * s) % N 
        nx = (x + dx8[d] * s) % N

        
       # print("y: " + str(y) + ", x:" + str(x))
        A[ny][nx] += 1
        visited[ny][nx] = True

        temp.append([ny,nx])
    
    for y,x in temp:
        sum = 0
        for d in range(4):
            ny = y + dy4[d]
            nx = x + dx4[d]
            if ( nx >= 0 and nx < N and ny >= 0 and ny < N):
                if A[ny][nx] > 0:
                    sum += 1
        #print(sum)
        A[y][x] += sum
    
    Cloud = []

    for y in range(N):
        for x in range(N):
            if not visited[y][x]:
                if A[y][x] >= 2:
                    Cloud.append([y,x])
                    A[y][x] -= 2
    
total = 0

for y in range(N):
        for x in range(N):
            total += A[y][x]

print(total)
   

  
