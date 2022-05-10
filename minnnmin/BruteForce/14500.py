def func():
    global n, m, graph
    result = 0

    #1 ㅡ
    if m >= 4:
        for i in range(n):          # 행
            for j in range(m-3):    # 열
                tmp = graph[i][j] + graph[i][j + 1] + graph[i][j + 2] + graph[i][j + 3]
                result = tmp if tmp > result else result

    if n >= 4:
        for i in range(n - 3):      # 행
            for j in range(m):      # 열
                tmp = graph[i][j] + graph[i + 1][j] + graph[i + 2][j] + graph[i + 3][j]
                result = tmp if tmp > result else result

    #2 ㅁ
    if n >= 2 and m >= 2:
        for i in range(n - 1):      # 행
            for j in range(m - 1):  # 열
                tmp = graph[i][j] + graph[i][j + 1] + graph[i + 1][j] + graph[i + 1][j + 1]
                result = tmp if tmp > result else result

    #3 ㄱ, ㄴ
    # 가로
    # ㄱ
    if m >= 3:
        for i in range(n - 1):      # 행
            for j in range(m - 2):  # 열
                # 시작점(i, j)은 꺾이는 부분
                tmp1 = graph[i][j] + graph[i][j + 1] + graph[i][j + 2] + graph[i + 1][j]
                tmp2 = graph[i][j] + graph[i][j + 1] + graph[i][j + 2] + graph[i + 1][j + 2]
                tmp = tmp1 if tmp1 > tmp2 else tmp2
                result = tmp if tmp > result else result
    # ㄴ
    if m >= 3:
        for i in range(1, n):       # 행
            for j in range(m - 2):  # 열
                tmp1 = graph[i][j] + graph[i][j + 1] + graph[i][j + 2] + graph[i - 1][j]
                tmp2 = graph[i][j] + graph[i][j + 1] + graph[i][j + 2] + graph[i - 1][j + 2]
                tmp = tmp1 if tmp1 > tmp2 else tmp2
                result = tmp if tmp > result else result

    # 세로
    # 오른쪽에 L
    if n >= 3:
        for i in range(n - 2):      # 행
            for j in range(m - 1):  # 열
                tmp1 = graph[i][j] + graph[i + 1][j] + graph[i + 2][j] + graph[i][j + 1]
                tmp2 = graph[i][j] + graph[i + 1][j] + graph[i + 2][j] + graph[i + 2][j + 1]
                tmp = tmp1 if tmp1 > tmp2 else tmp2
                result = tmp if tmp > result else result
    # 왼쪽에 J
    if n >= 3:
        for i in range(n - 2):      # 행
            for j in range(1, m):   # 열
                tmp1 = graph[i][j] + graph[i + 1][j] + graph[i + 2][j] + graph[i][j - 1]
                tmp2 = graph[i][j] + graph[i + 1][j] + graph[i + 2][j] + graph[i + 2][j - 1]
                tmp = tmp1 if tmp1 > tmp2 else tmp2
                result = tmp if tmp > result else result

    #4 ㄹ
    # 가로
    if m >= 3:
        for i in range(n - 1):      # 행
            for j in range(m - 2):  # 열
                # 시작점 (i, j)은 # 왼쪽 위
                tmp = graph[i][j] + graph[i][j + 1] + graph[i + 1][j + 1] + graph[i + 1][j + 2]
                result = tmp if tmp > result else result
    if m >= 3:
        for i in range(1, n):       # 행
            for j in range(m - 2):  # 열
                # 시작점 (i, j)은 # 왼쪽 아래
                tmp = graph[i][j] + graph[i][j + 1] + graph[i - 1][j + 1] + graph[i - 1][j + 2]
                result = tmp if tmp > result else result
    # 세로
    if n >= 3:
        for i in range(n - 2):      # 행
            for j in range(m - 1):  # 열
                # 시작점 (i, j)은 # 왼쪽 위
                tmp = graph[i][j] + graph[i + 1][j] + graph[i + 1][j + 1] + graph[i + 2][j + 1]
                result = tmp if tmp > result else result
    if n >= 3:
        for i in range(n - 2):  # 행
            for j in range(1, m):  # 열
                # 시작점 (i, j)은 # 오른쪽 위
                tmp = graph[i][j] + graph[i + 1][j] + graph[i + 1][j - 1] + graph[i + 2][j - 1]
                result = tmp if tmp > result else result

    #5
    # 가로
    # ㅗ
    if m >= 3:
        for i in range(1, n):       # 행
            for j in range(m - 2):  # 열
                # 시작점 (i, j)은 # 왼쪽
                tmp = graph[i][j] + graph[i][j + 1] + graph[i][j + 2] + graph[i - 1][j + 1]
                result = tmp if tmp > result else result
    # ㅜ
    if m >= 3:
        for i in range(n - 1):      # 행
            for j in range(m - 2):  # 열
                # 시작점 (i, j)은 # 왼쪽
                tmp = graph[i][j] + graph[i][j + 1] + graph[i][j + 2] + graph[i + 1][j + 1]
                result = tmp if tmp > result else result

    # 세로
    # ㅓ
    if n >= 3:
        for i in range(n - 2):      # 행
            for j in range(1, m):   # 열
                # 시작점 (i, j)은 # 맨 위
                tmp = graph[i][j] + graph[i + 1][j] + graph[i + 2][j] + graph[i + 1][j - 1]
                result = tmp if tmp > result else result
    # ㅏ
    if n >= 3:
        for i in range(n - 2):      # 행
            for j in range(m - 1):  # 열
                # 시작점 (i, j)은 # 맨 위
                tmp = graph[i][j] + graph[i + 1][j] + graph[i + 2][j] + graph[i + 1][j + 1]
                result = tmp if tmp > result else result

    return result

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
print(func())

# 의도치 않은 빡구현