import sys, copy

N, M, K = map(int, sys.stdin.readline().split())
fireballs = dict()
for _ in range(M):
    r, c, m, s, d = map(int, sys.stdin.readline().split())
    if (r - 1, c - 1) in fireballs:
        fireballs[(r - 1, c - 1)].append([m, s, d])
    else:
        fireballs[(r - 1, c - 1)] = [[m, s, d]]

new_fb = {}

# 0~7
dir_x = [-1, -1, 0, 1, 1, 1, 0, -1]
dir_y = [0, 1, 1, 1, 0, -1, -1, -1]

def calculate_pos(x):
    if x < 0:
        if x > -N:
            answer = x + N
        else:
            if -x % N == 0:
                answer = 0
            else:
                answer = x + N * (-x // N + 1)
    else: # x > 0
        answer = x % N
    return answer

for turn in range(K):
    # 1. move
    for key, value in fireballs.items():
        for m, s, d in value:
            r = key[0]
            c = key[1]
            r += dir_x[d] * s
            c += dir_y[d] * s
            if r < 0 or r >= N:
                r = calculate_pos(r)
            if c < 0 or c >= N:
                c = calculate_pos(c)
            # new_fb에 이동한 정보 추가
            if (r, c) in new_fb:
                new_fb[(r, c)].append([m, s, d])
            else:
                new_fb[(r, c)] = [[m, s, d]]
    # 2. divide
    for key, value in new_fb.items():
        add_list = []   # 원소: [m, s, d]
        if len(value) > 1:
            # 첫번째 파이어볼 정보
            total_m = value[0][0]
            total_s = value[0][1]
            until_dir = [value[0][2]]
            for m, s, d in value[1:]:
                total_m += m
                total_s += s
                until_dir.append(d)
            divide_m = total_m // 5
            divide_s = total_s // len(value)
            ex_d = until_dir[0]
            all_dir_same = True
            for now_d in until_dir[1:]: # ex_d랑 비교해서 모두 홀수이거나 짝수인지
                if (ex_d + now_d) % 2 == 0:
                    continue
                else:
                    all_dir_same = False
                    break
        else:
            continue
        if divide_m:
            if all_dir_same:
                final_dir = [0, 2, 4, 6]
            else:
                final_dir = [1, 3, 5, 7]
            for i in range(4):
                add_list.append([divide_m, divide_s, final_dir[i]])
        new_fb[key] = add_list
    if turn == K - 1:
        answer = 0
        for fb_list in new_fb.values():
            for fb in fb_list:
                answer += fb[0]
        print(answer)
    else:
        fireballs.clear()
        fireballs = copy.deepcopy(new_fb)
        new_fb.clear()