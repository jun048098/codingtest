n,m =map(int, input().split())
inf = int(1e9)
graph = [[inf] * (n+1) for _ in range(n+1)]
for i in range(n+1):
    graph[i][i] = 0

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

# 플로이드 워셜
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

answer = 0
for i in range(1, n+1):
    cnt = 0
    for j in range(1,n+1):
        if graph[i][j] != inf or graph[j][i]!= inf:
            cnt+=1
    if cnt == n:
        answer +=1
print(answer)

'''
6 6
1 5
3 4
4 2
4 6
5 2
5 4
'''