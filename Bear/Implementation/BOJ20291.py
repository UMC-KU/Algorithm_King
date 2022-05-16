import sys

N = int(sys.stdin.readline().rstrip())
dic = dict()

for _ in range(N):
    file = sys.stdin.readline().rstrip()
    kind = file.split(".")[-1]

    try:
        dic[kind]+=1
    except:
        dic[kind] = 1

key = sorted(dic.keys())

for k in key:
    print(k+" "+str(dic[k]))