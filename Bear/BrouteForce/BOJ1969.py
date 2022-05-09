import sys

N,M = map(int,sys.stdin.readline().rstrip().split())

DNA = []
ans = ""
cnt = 0

for _ in range(N):
    DNA.append(sys.stdin.readline().rstrip())

for i in range(M):
    s = [0,0,0,0]
    for j in range(N):
        if DNA[j][i] == 'A':
            s[0] += 1
        elif DNA[j][i] == 'C':
            s[1] += 1
        elif DNA[j][i] == 'G':
            s[2] += 1
        elif DNA[j][i] == 'T':
            s[3] += 1

    Hamming = max(s)
    temp = s.index(Hamming)
    cnt += N -Hamming

    if temp == 0:
        ans += 'A'
        
    elif temp == 1:
        ans += 'C'

    elif temp == 2:
        ans += 'G'
    elif temp == 3:
        ans += 'T'

print(ans)
print(cnt)