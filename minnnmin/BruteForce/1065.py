N = int(input())

def hansu(num):
    count = 0
    for i in range(1, num+1):
        if i <= 99:
            count += 1
        else:
            temp = list(map(int, str(i)))
            if temp[1] - temp[0] == temp[2] - temp[1]:
                count += 1
    print(count)

hansu(N)