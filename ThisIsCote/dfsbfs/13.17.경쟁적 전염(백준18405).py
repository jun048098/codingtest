from collections import deque
n, k = map(int, input().split())
graph = []
data = []
for i in range(n):
    graph.append(list(map(int, input().split())))
for x in range(n):
    for y in range(n):
        if graph[x][y] !=0 :
            data.append([graph[x][y],0,x,y])
data.sort()
q =deque(data)
# 정답 정보
v_s, v_x, v_y = map(int,input().split())

dx = [0,0,-1,1]
dy = [-1,1,0,0]

while q:
    v, s, x, y = q.popleft()
    if s == v_s:
        break
    for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx >= 0 and ny >= 0 and nx < n and ny < n :
                if graph[nx][ny] == 0:
                    graph[nx][ny] = v
                    q.append([v, s+1, nx, ny])

print(graph[v_x-1][v_y-1])