import sys


n, m = map(int, sys.stdin.readline().rstrip().split())

dict = {}

for i in range(1, n + 1):
    a =  sys.stdin.readline().rstrip()
    dict[i] = a
    dict[a] = i

for i in range(m):
    quest = sys.stdin.readline().rstrip()
    if quest.isdigit():
        print(dict[int(quest)])
    else:
        print(dict[quest])