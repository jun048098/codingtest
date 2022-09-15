from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int,input().strip())) for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
q = deque()
q.append((0,0))
while q :
    x , y= q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx <0 or ny <0 or nx >= n or ny >= m:
            continue
        elif graph[nx][ny] == 1:
            graph[nx][ny] += graph[x][y]
            q.append([nx,ny])
print(graph[n-1][m-1])
'''
4 6
101111
101010
101011
111011
'''