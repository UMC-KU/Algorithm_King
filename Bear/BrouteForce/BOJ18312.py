import sys

N,K = map(int,sys.stdin.readline().split())

h = 0
m = 0
s = 0

hh ="00"
mm = "00"
ss = "00"

ans = 0

while True:

    

    if h < 10:
        hh = "0"+str(h)
    else:
        hh = str(h)

    if m < 10:
        mm = "0"+str(m)
    else:
        mm = str(m)

    if s < 10:
        ss = "0"+str(s)
    else:
        ss = str(s)
    

    temp = hh+mm+ss
    if str(K) in temp:
        ans += 1
    
    if h == N and m == 59 and s == 59:
        break

    s += 1

    if s == 60:
        s = 0
        m +=1
    
    if m == 60:
        m = 0
        h += 1

print(ans)