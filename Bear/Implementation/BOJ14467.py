import sys

N = int(sys.stdin.readline().rstrip())
dic= dict()

total = 0

for _ in range(N):
    num, loc = map(int,sys.stdin.readline().rstrip().split())
    temp = -1
    try:
        temp = dic[num]
        if loc != temp:
            total += 1
            dic[num] = loc
    except:
        dic[num] = loc
    
print(total)
    