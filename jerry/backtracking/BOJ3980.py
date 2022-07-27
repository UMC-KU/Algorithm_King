def backtracking(depth, sum):
    global max_price
    # global check

    if depth == 11:
        if sum > max_price:
            max_price = sum
        return

    else:
        for i in range(11):
            # print("i", i)
            if check[i] == 1:
                continue
            if arr[depth][i] == 0:
                continue
            check[i] = 1
            sum += arr[depth][i]
            # print("depth", depth, "idx", i, "sum", sum)
            backtracking(depth + 1, sum)
            check[i] = 0
            sum -= arr[depth][i]


C = int(input())

while C > 0:
    arr = []
    max_price = 0
    check = [0] * 11
    for i in range(11):
        arr.append(list(map(int, input().split())))

    backtracking(0, 0)
    print(max_price)
    C -= 1
