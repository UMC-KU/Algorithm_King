import sys

keyboard = [['q','w','e','r','t','y','u','i','o','p'],['a','s','d','f','g','h','j','k','l','0'],['z','x','c','v','b','n','m','0','0','0']]

left , right = sys.stdin.readline().rstrip().split()
left_x = 0
left_y = 0
right_x = 0
right_y = 0
total_time = 0
for y in range(3):
        for x in range(10):
            if keyboard[y][x] == left:
                left_x = x
                left_y = y
            if keyboard[y][x] == right:
                right_x = x
                right_y = y

find = sys.stdin.readline().rstrip()

for st in find:

    for y in range(3):
        for x in range(10):

            if keyboard[y][x] == st:
                if (x <= 4 and y == 0) or (x <= 4 and y == 1) or (x <= 3 and y == 2):
                    left_diff = abs(left_x-x)+abs(left_y-y)
                    total_time+=left_diff+1
                    left_x = x
                    left_y = y
                else:
                    right_diff = abs(right_x-x)+abs(right_y-y)
                    total_time+=right_diff+1
                    right_x = x
                    right_y = y
                    

                break
    

print(total_time)