import sys

n,m,r = map(int,sys.stdin.readline().rstrip().split())

array = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]

for _ in range(r):
    for i in range(min(n,m)//2):
        x,y = i,i
        temp = array[y][x]

        # 왼쪽
        for j in range(i+1,n-i):
            y = j
            origin = array[y][x]
            array[y][x] = temp
            temp = origin
            print(array)
        
        #아래쪽
        for j in range(i+1,m-i):
            x = j
            origin = array[y][x]
            array[y][x] = temp
            temp = origin

        #우측
        for j in range(i+1,n-i):
            y = n-j-1
            origin = array[y][x]
            array[y][x] = temp
            temp = origin
        
        #위쪽
        for j in range(i+1,m-i):
            x = m-j-1
            origin = array[y][x]
            array[y][x] = temp
            temp = origin


for i in range(n):
    for j in range(m):
        print(array[i][j], end=' ')
    print()
