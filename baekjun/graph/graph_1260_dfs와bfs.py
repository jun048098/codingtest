from collections import deque

# 정점, 간선, 시작
n, m, v = map(int,input().split())
# 인접행렬
graph = [[0]*(n+1) for _ in range(n+1)]

for i in range(m):
    m1, m2 = map(int, input().split())
    graph[m1][m2] = graph[m2][m1] = 1

def dfs(start_v, discovered=[]):
    discovered.append(start_v)
    print(start_v, end=' ')

    for w in range(len(graph[start_v])):
        if graph[start_v][w] == 1 and(w not in discovered):
            dfs(w)

def bfs(start_v):
    discovered =[start_v]
    queue = deque()
    queue.append(start_v)

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for w in range(len(graph[start_v])):
            if graph[v][w] == 1 and (w not in discovered):
                discovered.append(w)
                queue.append(w)



dfs(v)
print()
bfs(v)