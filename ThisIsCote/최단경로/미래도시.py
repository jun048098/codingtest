import sys
inf = int(1e10)
input = sys.stdin.readline
n, m = map(int, input().strip().split())
graph = [[inf] * (n+1) for _ in range(n+1) ]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i ==j:
            graph[i][j]=0

for _ in range(m):
    a, b = map(int, input().strip().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

for k in range(n+1):
    for a in range(n+1):
        for b in range(n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

distance = graph[1][k] +graph[k][x]

if distance >= inf:
    print(-1)
else:
    print(distance)