n, m  =map(int, input().split())
graph = [list(map(int, input())) for i in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs (x,y):
    if x <= -1 or x >= n or y <=-1 or y >= m:
        return False

    if graph[x][y]==0:
        graph[x][y]=1
        for i in range(4):
            nx = dx[i]+x
            ny = dy[i]+y
            dfs(nx,ny)
        # dfs(x-1,y)
        # # dfs(x,y-1)
        # # dfs(x+1,y)
        # # dfs(x,y+1)
        return True
    return False

cnt = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) ==True:
            cnt+=1

print(cnt)
