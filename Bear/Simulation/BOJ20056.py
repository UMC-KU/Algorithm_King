import sys

N,M,K = map(int,sys.stdin.readline().rstrip().split())

dx = [0,1,1,1,0,-1,-1,-1]
dy = [1,1,0,-1,-1,-1,0,1]

fire = [[0 for _ in range(N)] for _ in range(N)]

print(fire)