import sys

N,M = map(int,sys.stdin.readline().rstrip().split())

a=[]

for _ in range(N):
    a.append(list(map(int,sys.stdin.readline().rstrip().split())))

ans = 0
for i in range(M):
    for j in range(i+1,M):
        for k in range(j+1,M):
            temp = 0
            for p in range(N):
                l = [a[p][i],a[p][j],a[p][k]]
                temp += max(l)
            ans = max(temp,ans)

print(ans)

