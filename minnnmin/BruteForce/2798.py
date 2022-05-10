import sys
from itertools import permutations

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

def jack(arr):
    gap = m
    result = 0
    for i in permutations(arr, 3):
        if sum(i) <= m and m - sum(i) < gap:
            gap = m - sum(i)
            result = sum(i)
    return result

print(jack(arr))