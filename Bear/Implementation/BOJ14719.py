import sys

H,W = map(int,sys.stdin.readline().rstrip().split())

block = list(map(int,sys.stdin.readline().rstrip().split()))

left = 0
temp = []
total = 0

for i in range(len(block)):
    if i == W-1:

        if left > block[i]:
            wall = max(temp)
            
       
            for rain in range(0,temp.index(wall)):
                if wall - rain > 0:
                    print(wall-temp[rain])
                    total += wall-temp[rain]
        
            break

    if left > block[i]:
        temp.append(block[i])
    
    else:
        wall = min(left,block[i])

        for rain in temp:
            if wall - rain > 0:
                print(wall-rain)
                total += wall-rain
        
        temp = []
        left = block[i]
       


print(total)