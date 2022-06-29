N = int(input())
graph = []
for _ in range(N):
    graph.append([])
cnt = 0
root = -1
for i in map(int, input().split()):
    if i == -1:
        root = cnt
    else:
        graph[i].append(cnt)
    cnt += 1

rm_node = int(input())
graph[rm_node] = [-1] # deleted
leaf_cnt = 0

for i in range(N):
    if rm_node in graph[i]:
        graph[i].remove(rm_node)

def dfs(root):
    global leaf_cnt
    if graph[root] == []:
        leaf_cnt += 1
    elif graph[root][0] == -1:
        return
    else:
        for node in graph[root]:
            dfs(node)
dfs(root)
print(leaf_cnt)