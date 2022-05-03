import sys

def make_mid_list(nums):
    result = []
    tmp = []
    cnt = 1
    for num in nums:
        tmp.append(num)
        if cnt % 2 == 1:
            tmp.sort()
            result.append(str(tmp[cnt // 2]))
        cnt += 1
    return result

t = int(input())
answer = []
cnt_list = []
for _ in range(t):
    n = int(sys.stdin.readline())
    if n % 2 == 0:
        cnt_list.append(n // 2)
    else:
        cnt_list.append(n // 2 + 1)
    if n > 10:
        n = n // 10 + 1
        nums = []
        for i in range(n):
            nums += list(map(int, sys.stdin.readline().split()))
    else:
        nums = list(map(int, sys.stdin.readline().split()))
    answer.append(make_mid_list(nums))

tmp = 0
for mid_list in answer:
    if len(mid_list) <= 10:
        print(cnt_list[tmp])
        print(' '.join(mid_list))
        tmp += 1
    else:
        print(cnt_list[tmp])
        if len(mid_list) % 10 == 0:
            for i in range(len(mid_list) // 10):
                print(' '.join(mid_list)[i * 10:i * 10 + 10])
        else:
            for i in range(len(mid_list) // 10 + 1):
                print(' '.join(mid_list[i * 10:i * 10 + 10]))
        tmp += 1