n, m = map(int, input().split())

graph = [[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    u, v = map(int, input().split())
    graph[u][v] = graph[v][u] = 1

visit = [0 for _ in range(n+1)]
cnt = 0

def dfs(start_v):
    visit.append(start_v)
    # print(start_v, end=' ')

    for m in range(len(graph[start_v])):
        if graph[start_v][m] == 1 and (visit != 0):
            dfs(m)

for j in range(1, n+1):
    if visit[i] == 0 and visit != 0: