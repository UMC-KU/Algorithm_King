import sys

N = int(sys.stdin.readline().rstrip())

TP = []

for _ in range(N):
    T,P = map(int,sys.stdin.readline().rstrip().split())
    TP.append((T,P))

dp=[0]*(N+1)

for i in range(N-1, -1, -1):
    day = TP[i][0]
    pay = TP[i][1]
    if day + i <= N:
        dp[i] = max(pay + dp[day+i], dp[i+1])
    else:
        dp[i] = dp[i+1]
            

print(dp[0])
