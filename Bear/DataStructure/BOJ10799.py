import sys
from tabnanny import check

laser = list(sys.stdin.readline().rstrip())

now = 0
answer = 0

check = False

for i in range(len(laser)):
    br = laser.pop()

    if br == ')':
        temp = laser.pop()
        if temp == ')':
            now += 1
        laser.append(temp)
        check = True
    else:
        if check:
            answer += now
        else:
            answer += 1
            now -= 1
        check = False

print(answer)
    