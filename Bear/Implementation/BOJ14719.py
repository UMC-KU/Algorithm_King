import sys

H,W = map(int,sys.stdin.readline().rstrip().split())

block = list(map(int,sys.stdin.readline().rstrip().split()))

left = 0
total = 0

for i in range(len(block)):

    max_left = max(block[:i+1])
    max_right = max(block[i:])
    m = min(max_left,max_right)
    total += abs(block[i] - m)
       
print(total)