import sys

n = int(sys.stdin.readline().rstrip())
dp = [0] * (n + 1)
dp[0], dp[1] = 0, 1

for i in range(2, n + 1):
    temp = 1e9
    j = 1
    while (j ** 2) <= i:
        temp = min(temp, dp[i - (j ** 2)])
        j += 1
    dp[i] = temp + 1

print(dp[n])