import math
import sys

dict = {}

total_tree = 0

while True:
    tree = sys.stdin.readline().rstrip()

    if tree == '':
        break

    try:
        dict[tree] += 1
    except:
        dict[tree] = 1
    
    total_tree += 1
    
temp_list = list(dict.keys())
temp_list.sort()

for i in temp_list:
    temp = dict[i]
    temp /= total_tree
    temp *= 100
    temp = round(temp,4)
    print(i+" %.4f" %temp)