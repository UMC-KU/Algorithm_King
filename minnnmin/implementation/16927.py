# boj 16927
import sys

N, M, rotate_cnt = map(int, input().split())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))

# layers 배열에 바깥쪽 껍질부터 보관
#   layer 크기 만큼만 rotate 해야 함
#   smaller 가 홀수면 마지막 원소는 회전시키지 말아야 함

layers = []
smaller = N if N < M else M
layer = smaller // 2
if smaller % 2 == 0:
    # layers 배열 생성
    for l in range(layer):
        # 위
        tmp = matrix[l][l:M - l]
        # 우
        for right in range(N - 2 - l*2):
            tmp.append(matrix[right + l + 1][M - 1 - l])
        # 아래
        tmp += list(reversed(matrix[N - 1 - l][l:M - l]))
        # 좌
        for left in range(N - 2 - l * 2):
            tmp.append(matrix[N - 1 - (l+1) - left][l])
        layers.append(tmp)
else:
    # layers 배열 생성
    for l in range(layer):
        # 위
        tmp = matrix[l][l:M - l]
        # 우
        for right in range(N - 2 - l * 2):
            tmp.append(matrix[right + 1][M - 1 - l])
        # 아래
        tmp += list(reversed(matrix[N - 1 - l][l:M - l]))
        # 좌
        for left in range(N - 2 - l * 2):
            tmp.append(matrix[N - 1 - left - 1][l])
        layers.append(tmp)
    # layer 만큼만 append 하고 마지막에 가장 안쪽 껍질 추가
    tmp = []
    if smaller == N:
        for col in range(M - 2 * layer):
            tmp.append(matrix[smaller // 2][layer + col])
    else:
        for row in range(N - 2 * layer):
            tmp.append(matrix[layer + row][smaller // 2])
    layers.append(tmp)

# rotate
new_layers = []
for l in range(layer):
    if len(layers[l]) > rotate_cnt:
        new_layers.append(layers[l][rotate_cnt:] + layers[l][0:rotate_cnt])
    else:
        tmp_rotate_cnt = rotate_cnt % len(layers[l])
        new_layers.append(layers[l][tmp_rotate_cnt:] + layers[l][0:tmp_rotate_cnt])
if smaller % 2 == 1:
    new_layers.append(layers[-1])

# rollback
new_matrix = []
for i in range(N):
    tmp = []
    for j in range(M):
        tmp.append(0)
    new_matrix.append(tmp)
for l in range(layer):
    # 윗줄 추가
    for i in range(M - l*2):
        new_matrix[l][i + l] = new_layers[l][i]
    # 오른쪽 추가
    for right in range(N - 2 - l*2):
        new_matrix[l + 1 + right][M - 1 - l] = new_layers[l][(M - l*2) + right]
    # 아래 추가
    start_idx = len(new_layers[l]) // 2
    for col in range(M - l*2):
        new_matrix[N - 1 - l][M - 1 - l - col] = new_layers[l][start_idx + col]
    # 왼쪽 추가
    for left in range(N - 2 - l*2):
        new_matrix[l + 1 + left][l] = new_layers[l][-(left + 1)]

if smaller % 2 == 1: #맨 안쪽 거 추가해줘야 함
    if smaller == N:
        for i in range(M - layer*2):
            new_matrix[N//2][layer + i] = new_layers[-1][i]
    else:
        for j in range(N - layer*2):
            new_matrix[M//2][layer + j] = new_layers[-1][i]
for row in new_matrix:
    print(*row)