import sys

N = int(sys.stdin.readline().rstrip())

TP = []

for _ in range(N):
    T,P = map(int,sys.stdin.readline().rstrip().split())
    TP.append((T,P))

dp=[0]*(N+1)

for i in range(0,N):

    for j in range(i+1):
        if i - TP[j][0] >= -1 and j + TP[j][0] - 1 <= i:
            dp[i] = max(dp[i - TP[j][0]]+TP[j][1],dp[i])
            print(str(dp[i])+" i:"+str(i))

print(dp[N-1])
