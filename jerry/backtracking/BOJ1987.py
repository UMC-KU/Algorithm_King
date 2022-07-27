import string

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
answer = 0


def dfs(now_pos, now_cnt):
    global answer
    answer = max(answer, now_cnt)
    for i in range(4):
        next_y = now_pos[0] + dy[i]
        next_x = now_pos[1] + dx[i]
        # print(ord(map[next_y][next_x]))
        if next_y < 0 or next_y > R - 1 or next_x < 0 or next_x > C - 1:
            continue
        # if check[next_y][next_x] == 1:
        #     continue
        if arr[ord(map[next_y][next_x]) - 65] == 1:
            continue
        # check[next_y][next_x] = 1
        arr[ord(map[next_y][next_x]) - 65] = 1
        dfs((next_y, next_x), now_cnt + 1)
        # check[next_y][next_x] = 0
        arr[ord(map[next_y][next_x]) - 65] = 0


R, C = map(int, input().split())
arr = [False for i in range(len(string.ascii_uppercase))]
map = []
# check = [[0] * C for i in range(R)]  # 방문했는지를 체크하는 배열
# visited = [[False]*C for _ in range(R)] <- 이렇게 하자
for i in range(R):
    map.append(list(input()))

now_pos = (0, 0)
now_cnt = 1
# check[now_pos[0]][now_pos[1]] = 1
arr[ord(map[now_pos[0]][now_pos[1]]) - 65] = 1


dfs(now_pos, now_cnt)
print(answer)
