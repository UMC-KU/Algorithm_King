N = int(input())

def func(num):
    for i in range(1, num):
        tmp = list(map(int, str(i)))
        arr = list(map(int, tmp))

        if i + sum(arr) == num:
            return i
    return 0

print(func(N))