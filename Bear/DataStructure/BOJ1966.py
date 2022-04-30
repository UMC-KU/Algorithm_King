import sys
from collections import deque

test = int(sys.stdin.readline().rstrip())

for _ in range(test):
    n,m = list(map(int, sys.stdin.readline().rstrip().split( )))
    imp = deque(list(map(int, sys.stdin.readline().rstrip().split( ))))
    idx = deque(list(range(len(imp))))
    idx[m] = 'target'

    # 순서
    order = 0
    
    while True:
        # 첫번째 if: imp의 첫번째 값 = 최댓값?
        if imp[0]==max(imp):
            order += 1
                        
            # 두번째 if: idx의 첫 번째 값 = "target"?
            if idx[0]=='target':
                print(order)
                break
            else:
                imp.popleft()
                idx.popleft()

        else:
            imp.append(imp.popleft())
            idx.append(idx.popleft())     