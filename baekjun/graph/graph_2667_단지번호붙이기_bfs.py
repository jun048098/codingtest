from collections import deque
n = int(input())
graph = [list(map(int,input().strip())) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    q = deque()
    q.append((x, y))
    graph[x][y] = 0
    cnt =1
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            if graph[nx][ny] ==1:
                cnt +=1
                q.append((nx,ny))
                graph[nx][ny]=0
    return cnt
apart = []
for i in range(n):
    for j in range(n):
        if graph[i][j] ==1:
            apart.append(bfs(i,j))
apart.sort()
print(len(apart))
for i in apart:
    print(i)
