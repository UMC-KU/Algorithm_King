import sys

n = int(sys.stdin.readline().rstrip())

sequence = []
answer = []
stack = []
now = 0

check = True

for i in range(n):
    sequence.append(int(sys.stdin.readline().rstrip()))


for num in sequence:

    while now < num:
        now += 1
        stack.append(now)
        answer.append("+")
    
    if stack[-1] == num:
        stack.pop()
        answer.append("-")
    else:
        check = False
        print("NO")
        break

if check:
    for str in answer:
        print(str)