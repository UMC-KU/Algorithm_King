import heapq
import sys

n = int(sys.stdin.readline().rstrip())
heap = []
ans = []

for _ in range(n):
    x = int(sys.stdin.readline().rstrip())
    if x == 0:
        try:
            ans.append(heapq.heappop(heap)[1])
        except:
            ans.append(0)
    else:
        heapq.heappush(heap,(x.__abs__(),x))

for a in ans:
    print(a)
    