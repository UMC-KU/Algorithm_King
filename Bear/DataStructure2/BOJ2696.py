from ntpath import join
import sys
import heapq

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    M = int(sys.stdin.readline().rstrip())
    num = []
    for i in range(M//10+1):
        num += list(map(int,sys.stdin.readline().rstrip().split()))
    temp = []
    ans = []

    for i in range(len(num)):
        temp.append(num[i])
        if i % 2 == 0:
            temp.sort()
            ans.append(temp[i // 2])
            
    print(len(ans))

    temp_str = ""

    for i in range(len(ans)):
        temp_str += str(ans[i]) + " "
        if i % 10 == 9:
            temp_str += "\n"
    
    print(temp_str)
