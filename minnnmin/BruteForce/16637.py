from collections import deque


def solution(rc, operations):
    answer = [[]]
    r = len(rc)
    c = len(rc[0])
    queue = deque()
    for row in rc:
        queue.append(deque(row))

    for op in operations:
        if op == "ShiftRow":
            last_row = queue[-1]
            queue.pop()
            queue.appendleft(last_row)
        else:  # Rotate
            queue = rotate(queue, r, c)

    return queue


def rotate(queue, r, c):
    tmp = queue[0][0]

    # 1. 왼쪽 열
    for i in range(1, r):
        queue[i - 1][0] = queue[i][0]
    # 2. 맨 아래
    queue[-1].popleft()
    tmp_row = queue[-1]
    tmp_row.append(-1)
    queue.pop()
    queue.append(tmp_row)
    # 2. 오른쪽 열
    for i in range(r - 2, -1, -1):
        queue[i + 1][c - 1] = queue[i][c - 1]
    # 맨 윗줄
    tmp2 = deque([queue[0][0], tmp])
    queue[0].popleft()
    queue[0].pop()
    first_row = tmp2 + queue[0]
    result = deque()
    result.append(first_row)
    queue.popleft()
    result += queue
    return result

answer = solution([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], ["ShiftRow", "Rotate", "ShiftRow", "Rotate"])
answer_list = []
for i in answer:
    answer_list.append([*i])
print(answer_list)