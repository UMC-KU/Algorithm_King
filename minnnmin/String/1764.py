import sys

n, m = map(int, input().split())
no_hear = set()
no_see = set()

for _ in range(n):
    no_hear.add(sys.stdin.readline().rstrip())
for _ in range(m):
    no_see.add(sys.stdin.readline().rstrip())

result = sorted(list(no_hear & no_see))
print(len(result))
for i in result:
    print(i)