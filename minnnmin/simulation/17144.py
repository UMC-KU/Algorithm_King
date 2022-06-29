import sys

R, C, T = map(int, sys.stdin.readline().split())
origin_matrix = []
copy_matrix = []
for _ in range(R):
    origin_matrix.append(list(map(int, sys.stdin.readline().split())))
    copy_matrix.append([0] * C)

air_cleaner = []  # x좌표만 저장
dust_pos = []

for r in range(R):
    for c in range(C):
        if origin_matrix[r][c] != 0:
            if origin_matrix[r][c] == -1:
                air_cleaner.append(r)
            else:
                dust_pos.append((r, c))

for _ in range(T):
    # <diffusion>
    for d_pos in dust_pos:
        possible_dir_cnt = 0
        possible_dir_pos = []
        x = d_pos[0]
        y = d_pos[1]

        if 0 <= x-1 < R and 0 <= y < C:
            if y == 0:
                if x-1 != air_cleaner[0] and x-1 != air_cleaner[1]:
                    possible_dir_cnt += 1
                    possible_dir_pos.append((x - 1, y))
            else:
                possible_dir_cnt += 1
                possible_dir_pos.append((x - 1, y))
        if 0 <= x+1 < R and 0 <= y < C:
            if y == 0:
                if x+1 != air_cleaner[0] and x+1 != air_cleaner[1]:
                    possible_dir_cnt += 1
                    possible_dir_pos.append((x + 1, y))
            else:
                possible_dir_cnt += 1
                possible_dir_pos.append((x + 1, y))
        if 0 <= x < R and 0 <= y-1 < C:
            if y - 1 == 0:
                if x != air_cleaner[0] and x != air_cleaner[1]:
                    possible_dir_cnt += 1
                    possible_dir_pos.append((x, y - 1))
            else:
                possible_dir_cnt += 1
                possible_dir_pos.append((x, y - 1))
        if 0 <= x < R and 0 <= y+1 < C:
            if y + 1 == 0:
                if x != air_cleaner[0] and x != air_cleaner[1]:
                    possible_dir_cnt += 1
                    possible_dir_pos.append((x, y + 1))
            else:
                possible_dir_cnt += 1
                possible_dir_pos.append((x, y + 1))

        if possible_dir_cnt:
            dust = origin_matrix[x][y] // 5
            for pos in possible_dir_pos:
                copy_matrix[pos[0]][pos[1]] += dust
            origin_matrix[x][y] -= dust * possible_dir_cnt
        possible_dir_cnt = 0
        possible_dir_pos.clear()

    # <original += copy>
    for r in range(R):
        for c in range(C):
            if copy_matrix[r][c] != 0 and copy_matrix[r][c] != -1:
                origin_matrix[r][c] += copy_matrix[r][c]
    copy_matrix.clear()
    for _ in range(R):  # reset
        copy_matrix.append([0] * C)

    # <move>
    # counterclockwise: start at air_cleaner[0]
    # 1) left
    for x in range(air_cleaner[0] - 2, -1, -1):
        origin_matrix[x + 1][0] = origin_matrix[x][0]
    # 2) up
    for y in range(1, C):
        origin_matrix[0][y - 1] = origin_matrix[0][y]
    # 3) right
    for x in range(1, air_cleaner[0] + 1):
        origin_matrix[x - 1][C - 1] = origin_matrix[x][C - 1]
    # 4) down
    for y in range(C - 2, 0, -1):
        origin_matrix[air_cleaner[0]][y + 1] = origin_matrix[air_cleaner[0]][y]
    origin_matrix[air_cleaner[0]][1] = 0  # 젤 마지막 0 채우기

    # clockwise: start at air_cleaner[1]
    # 1) left
    for x in range(air_cleaner[1] + 2, R):
        origin_matrix[x - 1][0] = origin_matrix[x][0]
    # 2) down
    for y in range(1, C):
        origin_matrix[R - 1][y - 1] = origin_matrix[R - 1][y]
    # 3) right
    for x in range(R - 2, air_cleaner[1] - 1, -1):
        origin_matrix[x + 1][C - 1] = origin_matrix[x][C - 1]
    # 4) up
    for y in range(C - 2, 0, -1):
        origin_matrix[air_cleaner[1]][y + 1] = origin_matrix[air_cleaner[1]][y]
    origin_matrix[air_cleaner[1]][1] = 0  # 젤 마지막 0 채우기

    # update dust_pos
    dust_pos.clear()
    for r in range(R):
        for c in range(C):
            if origin_matrix[r][c] != 0 and origin_matrix[r][c] != -1:
                dust_pos.append((r, c))

dust_sum = 2 # 공기청정기 값 -1씩이니까
for row in origin_matrix:
    dust_sum += sum(row)
print(dust_sum)