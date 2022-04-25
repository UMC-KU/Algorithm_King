import sys

N,K = list(map(int,sys.stdin.readline().rstrip().split()))

list = []
answer = []

for i in range(1,N+1):
    list.append(i)

num = 0

while len(list):
    #for i in range(0,K-1): #이중 반복문으로 시간복잡도가 O(n^2)이 되어버림
    #    list.append(list.pop(0))
    #answer.append(str(list.pop(0)))
    num+=(K-1)
    if num >= len(list):
        num %= len(list)
    answer.append(str(list[num]))
    list.pop(num)


answerStr = "<"

for i in range(0,N):
    if(i != N-1):
        answerStr += str(answer[i]) + ", "
    else:
        answerStr += str(answer[i]) + ">"
print(answerStr)