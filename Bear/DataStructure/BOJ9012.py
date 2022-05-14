import sys

N = int(sys.stdin.readline().rstrip())

string = []

for i in range(N):
    string.append(sys.stdin.readline().rstrip())


for i in range(N):
    temp = []
    check = True

    for ch in string[i]:
        if ch == "(":
            temp.append("(")
        else:
            try:
                temp.pop()
            except:
                check = False
                break
    if len(temp) != 0:
        check = False
    
    if (check):
        print("YES")
    else:
        print("NO")
