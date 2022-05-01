from collections import deque
import sys


N = int(sys.stdin.readline().rstrip())
Balloon =deque(enumerate(map(int, sys.stdin.readline().rstrip().split())))
# 인덱스와 값 동시 저장
answer = []

while len(Balloon) != 0:
    idx,num = Balloon.popleft()

    answer.append(idx+1)

    if num > 0:
        Balloon.rotate(-(num - 1))
    else:
        Balloon.rotate(-(num))

print(' '.join(map(str, answer)))
