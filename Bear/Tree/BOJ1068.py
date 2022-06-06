from collections import deque
import sys

N = int(sys.stdin.readline().rstrip())

temp = list(map(int,sys.stdin.readline().rstrip().split()))

remove = int(sys.stdin.readline().rstrip())

graph = [[] for i in range(N)]
visited = [False for _ in range(N)]

parent_node = 0

for i in range(N):
    if temp[i] != -1:
        graph[i].append(temp[i])
        graph[temp[i]].append(i)
    else:
        parent_node = i

answer = 0

def bfs(p):
    global answer
    q = deque()
    q.append(p)
    visited[p] = True

    while len(q) != 0:
        now = q.popleft()
        for link in graph[now]:
            if link != remove and not visited[link]:
                q.append(link)
                visited[link] = True
            if link == remove:
                if len(graph[now]) == 2 and now != parent_node:
                    answer+=1
                if len(graph[now]) == 1 and now == parent_node:
                    answer+=1

        if (len(graph[now]) == 1 and now != parent_node):
            answer += 1

if remove != parent_node:
    bfs(parent_node)



print(answer)
