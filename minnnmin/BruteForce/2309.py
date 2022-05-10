import sys

nanjangee = []
for _ in range(9):
    nanjangee.append(int(sys.stdin.readline().rstrip()))

sum_of_nanjangee = sum(nanjangee)
flag = False
for i in range(8):
    for j in range(i+1, 9):
        t1 = nanjangee[i]
        t2 = nanjangee[j]

        if sum_of_nanjangee - t1 - t2 == 100:
            flag = True
            nanjangee.remove(t1)
            nanjangee.remove(t2)
            break
    if flag:
        break

nanjangee.sort()
for nan in nanjangee:
    print(nan)