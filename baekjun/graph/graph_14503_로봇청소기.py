import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
n, m = map(int, input().strip().split())
# d 북쪽:0, 동쪽:1, 남쪽:2, 서쪽:3
r, c, d = map(int, input().strip().split())
move = [[-1,0],[0,1],[1,0],[0,-1]]
graph = [list(map(int, input().strip().split())) for i in range(n)]
cnt = 0
def dfs(x, y, d):
    global cnt
    if graph[x][y]==0:
        graph[x][y] +=2
        cnt+=1
    for i in range(4):
        d = (d+3)%4
        nx = x +move[d][0]
        ny = y +move[d][1]
        if nx <0 or ny<0 or nx >=n or ny>=m:
            continue
        # if graph[nx][ny] == 1:
        #     continue
        if graph[nx][ny] == 0:
            dfs(nx, ny, d)
            return
    bx= x-move[d][0]
    by = y - move[d][1]
    if graph[bx][by] != 1:
        dfs(bx, by, d)
dfs(r, c, d)
print(cnt)
# for i in graph:
#     print(i)

