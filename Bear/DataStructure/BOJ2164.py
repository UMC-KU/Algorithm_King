import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())

list =deque([i for i in range(1,N+1)])

# for i in range(1,N): #시간 오류
#     list.pop(0)
#     list.append(list.pop(0))

temp = 2

while len(list) > 1: 
    list.popleft()
    list.append(list.popleft())




print(list[0])