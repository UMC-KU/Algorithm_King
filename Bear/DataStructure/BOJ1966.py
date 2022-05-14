import sys
from collections import deque

test = int(sys.stdin.readline().rstrip())

for _ in range(test):
    n,m = list(map(int, sys.stdin.readline().rstrip().split( )))
    imp = deque(list(map(int, sys.stdin.readline().rstrip().split( ))))
    idx = deque(list(range(len(imp))))
    idx[m] = 'target'

    order = 0
    
    while True:
        if imp[0]==max(imp):
            order += 1
                        
            if idx[0]=='target':
                print(order)
                break
            else:
                imp.popleft()
                idx.popleft()

        else:
            imp.append(imp.popleft())
            idx.append(idx.popleft())     