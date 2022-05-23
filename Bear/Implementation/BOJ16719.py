import sys

zoac = sys.stdin.readline().rstrip()

if len(zoac) == 1:
    print(zoac)
    sys.exit()

dic = []

for i in range(0,len(zoac)):
    dic.append((zoac[i],i))

dic = sorted(dic)

ans = [0 for _ in range(len(zoac))]
ans[dic[0][1]] = dic[0][0]
del dic[0]

while len(dic) > 0:
    print(''.join([st for st in ans if st != 0]))
    
    i = 0
    idx = 0
    min = ['z']*len(dic)

    while i < len(dic):
        temp = ans.copy()
        temp[dic[i][1]] = dic[i][0]

        if ''.join([st for st in min if st != 0]) > ''.join([st for st in temp if st != 0]):
            min = temp
            idx = i
        i += 1

    ans = min
    del dic[idx]

print(zoac)

