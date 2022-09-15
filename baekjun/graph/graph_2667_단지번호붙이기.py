import sys
input = sys.stdin.readline
n = int((input()))
graph = [list(map(int,input().strip())) for _ in range(n)]
m = len(graph[0])
visit = [[False for _ in range(m)]for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x,y):
    visit[x][y] =True
    for i in range(4):
        nx = x +dx
        ny = y +dy
        if nx<0 or ny<0 or nx>=n or ny>=m:
            continue
        elif visit[nx][ny]:
            continue
        elif visit[nx][ny] ==False:
            visit[nx][ny] = True

