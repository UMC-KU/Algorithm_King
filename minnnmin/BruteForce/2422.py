import sys

N, M = map(int, sys.stdin.readline().split())
no_mix = set()
count = 0

# 이 쌍이 no_mix에 있는지 검사
def dont_mix(a, b):
    if (a, b) in no_mix or (b, a) in no_mix:
        return True
    return False

if N < 3:
    print(count)
else:
    for i in range(M):
        a, b = map(int, sys.stdin.readline().split())
        tmp = (a, b)
        no_mix.add(tmp)

    for i in range(1, N+1):
        for j in range(i+1, N+1):
            if dont_mix(i, j):
                continue
            for k in range(j+1, N+1):
                if dont_mix(i, k) or dont_mix(j, k):
                    continue
                count += 1
    print(count)

# no_mix를 list에서 set으로 바꾸고 나서야 통과
# list는 엄 청 느리다