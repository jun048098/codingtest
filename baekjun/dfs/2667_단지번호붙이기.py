n = int(input())
graph = [list(map(int, input())) for i in range(n)]
visited  = [[0]*n for _ in range(n)]
apart = []
# 방향
dx = [-1, 1, 0, 0]
dy = [0,0, 1, -1]

def dfs(x,y,c):
    visited[x][y] = 1
    global nums
    if graph[x][y] ==1:
        graph[x][y] =c
        nums +=1
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<= nx <n and 0<= ny < n:
            if visited[nx][ny] == 0 and graph[nx][ny] ==i:
                dfs(nx, ny, c)

cnt  = 1
numlist = []
nums = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == 0:
            dfs(i,j,cnt)
            nums = 0

print(len(numlist))
for i in sorted(numlist):
    print(i)
