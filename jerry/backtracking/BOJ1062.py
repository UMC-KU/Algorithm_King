import sys
import string

# input = sys.stdin.readline  # 일케 하면 되나?


def backtracking(depth, cnt):
    global answer
    if cnt == K - 5:
        readable = 0
        for word in arr:
            able = True
            for a in word:
                if not check[ord(a) - 97]:
                    able = False
                    break
            if able:
                readable += 1

        answer = max(answer, readable)
        return

    for i in range(depth, len(string.ascii_lowercase)):
        if not check[i]:
            check[i] = True
            backtracking(i, cnt + 1)
            check[i] = False


N, K = map(int, input().split())

if K < 5:
    print(0)
    exit()
else:
    arr = []
    for _ in range(N):
        arr.append(input().rstrip())
    # print(arr)

    check = [False] * len(string.ascii_lowercase)
    # a,n,t,i,c 5개는 무조건 있어야 함
    for i in ["a", "n", "t", "i", "c"]:
        check[ord(i) - 97] = True

    answer = 0
    backtracking(0, 0)
    print(answer)
