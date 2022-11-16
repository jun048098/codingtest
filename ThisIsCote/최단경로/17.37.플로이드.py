import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
inf = int(1e9)
graph = [[inf] * (n+1)  for _ in range(n+1)]
for i in range(1,n+1):
    graph[i][i] = 0

for i in range(m):
    a, b, c = map(int, input().split())
    if c <graph[a][b]:
        graph[a][b] = c
# 플로이드 워셜
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][k]+ graph[k][b], graph[a][b])


for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == inf:
            print(0, end=" ")
        else:
            print(graph[i][j] , end= ' ')
    print()