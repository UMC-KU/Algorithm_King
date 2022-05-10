import sys

n = int(sys.stdin.readline().rstrip())
cnt = 0
while True:
    cnt += 1
    n -= int(n**0.5)**2
    if n == 0:
        break
print(cnt)