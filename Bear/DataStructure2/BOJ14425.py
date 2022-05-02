import sys
input = sys.stdin.readline

N, M = map(int, sys.stdin.readline().rstrip().split())
str = set([sys.stdin.readline().rstrip() for _ in range(N)])
cnt = 0

for _ in range(M):

    temp = sys.stdin.readline().rstrip()

    if temp in str:
        cnt += 1

print(cnt)