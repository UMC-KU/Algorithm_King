import sys

N = int(sys.stdin.readline().rstrip())

for i in range(1,1000001):
    sum = i
    temp = i
    if temp >= 10:
        while temp >= 1:
            sum += temp % 10
            temp //= 10
    if sum == N:
        print(i)
        exit()

print(0)


        