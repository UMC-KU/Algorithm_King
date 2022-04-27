
import sys
import math

N = int(sys.stdin.readline().rstrip())
arith = sys.stdin.readline().rstrip()

num = []

list = []

for i in range(N):
    num.append(int(sys.stdin.readline().rstrip()))

for ch in arith:
    if ch == '*':
        temp2 = list.pop()
        temp1 = list.pop()
        list.append(temp1*temp2)
    elif ch == '+':
        temp2 = list.pop()
        temp1 = list.pop()
        list.append(temp1+temp2)
    elif ch == '-':
        temp2 = list.pop()
        temp1 = list.pop()
        list.append(temp1-temp2)
    elif ch == '/':
        temp2 = list.pop()
        temp1 = list.pop()
        list.append(temp1/temp2)
    else:
        list.append(num[ord(ch)-65])
    
print('%.2f' %list[0])