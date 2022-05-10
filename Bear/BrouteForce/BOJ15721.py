import sys

A = int(sys.stdin.readline().rstrip())
T = int(sys.stdin.readline().rstrip())
bin = int(sys.stdin.readline().rstrip())

temp = 0
n = 2 #번데기 반복횟수
m = 0 #bin이 나온 횟수
people = 0
list = []


while True:
    list += [0,1,0,1]

    for _ in range(n):
        list.append(0)

    for _ in range(n):
        list.append(1)
    
    if len(list) // 2 >= T:
        for i in range(len(list)):
            temp += 1
            if list[i] == bin:
                m += 1
                if m == T:
                    print(i % A)
                    break
    else :
        n += 1
        continue
    
    break
