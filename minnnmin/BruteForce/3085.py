import sys

n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(sys.stdin.readline().rstrip()))
cols = []
for _ in range(n):
    cols.append([])
for i, c in enumerate(matrix):
    cols[i].append(c)

# original cnt
candy_cnt = set()
for row in matrix:
    candy = row[0]
    cnt = 0
    for c in row:
        if c == candy:
            cnt += 1
        else:
            candy_cnt.add(cnt)
            candy = c
            cnt = 1
    candy_cnt.add(cnt)

for col in cols:
    candy = row[0]
    cnt = 0
    for c in col:
        if c == candy:
            cnt += 1
        else:
            candy_cnt.add(cnt)
            candy = c
            cnt = 1
    candy_cnt.add(cnt)

def matrix_search(matrix, n):
    # row
    answer = 1
    for r in range(n - 1):
        for c in range(n):
            matrix[r][c], matrix[r + 1][c] = matrix[r + 1][c], matrix[r][c]
            # 바꿨으니 검사 3번 => 이번행, 다음행, 해당열
            candy = matrix[r][0]
            cnt = 1
            for i in range(1, n):
                if matrix[r][i] == candy:
                    cnt += 1
                else:
                    if cnt > answer:
                        answer = cnt
                        candy = matrix[r][i]
                        cnt = 1
                    else:
                        candy = matrix[r][i]
                        cnt = 1
            if cnt == n:
                return n
            if cnt > answer:
                answer = cnt
            if answer == n:
                return answer

            candy = matrix[r + 1][0]
            cnt = 1
            for i in range(1, n):
                if matrix[r + 1][i] == candy:
                    cnt += 1
                else:
                    if cnt > answer:
                        answer = cnt
                        candy = matrix[r + 1][i]
                        cnt = 1
                    else:
                        candy = matrix[r + 1][i]
                        cnt = 1
            if cnt == n:
                return n
            if cnt > answer:
                answer = cnt
            if answer == n:
                return answer

            # 해당 열 검사
            candy = matrix[0][c]
            cnt = 1
            for i in range(1, n):
                if matrix[i][c] == candy:
                    cnt += 1
                else:
                    if cnt > answer:
                        answer = cnt
                        candy = matrix[i][c]
                        cnt = 1
                    else:
                        candy = matrix[i][c]
                        cnt = 1
            if cnt == n:
                return n
            if cnt > answer:
                answer = cnt
            if answer == n:
                return answer
            matrix[r][c], matrix[r + 1][c] = matrix[r + 1][c], matrix[r][c]

    # col
    for c in range(n - 1):
        for r in range(n):
            matrix[r][c], matrix[r][c + 1] = matrix[r][c + 1], matrix[r][c]
            # 바꿨으니 검사 3번 => 이번열, 다음열, 해당행
            candy = matrix[0][c]
            cnt = 1
            for i in range(1, n):
                if matrix[i][c] == candy:
                    cnt += 1
                else:
                    if cnt > answer:
                        answer = cnt
                        candy = matrix[i][c]
                        cnt = 1
                    else:
                        candy = matrix[i][c]
                        cnt = 1
            if cnt == n:
                return n
            if cnt > answer:
                answer = cnt
            if answer == n:
                return answer

            candy = matrix[0][c + 1]
            cnt = 1
            for i in range(1, n):
                if matrix[i][c + 1] == candy:
                    cnt += 1
                else:
                    if cnt > answer:
                        answer = cnt
                        candy = matrix[i][c + 1]
                        cnt = 1
                    else:
                        candy = matrix[i][c + 1]
                        cnt = 1
            if cnt == n:
                return n
            if cnt > answer:
                answer = cnt
            if answer == n:
                return answer

            # 해당 행 검사
            candy = matrix[r][0]
            cnt = 1
            # answer = 1
            for i in range(1, n):
                if matrix[r][i] == candy:
                    cnt += 1
                else:
                    if cnt > answer:
                        answer = cnt
                        candy = matrix[r][i]
                        cnt = 1
                    else:
                        candy = matrix[r][i]
                        cnt = 1
            if cnt == n:
                return n
            if cnt > answer:
                answer = cnt
            if answer == n:
                return answer
            matrix[r][c], matrix[r][c + 1] = matrix[r][c + 1], matrix[r][c]
    return answer

tmp = max(candy_cnt)
if tmp == n:
    print(n)
else:
    tmp2 = matrix_search(matrix, n)
    if tmp >= tmp2:
        print(tmp)
    else:
        print(tmp2)

# 코드 길이보니 길을 잘못든 거 같다 (실버3 맞아?)