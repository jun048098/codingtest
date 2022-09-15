from collections import deque
n,m = 5,6
graph=[[1,0,1,0,1,0],
        [1,1,1,1,1,1],
        [0,0,0,0,0,1],
        [1,1,1,1,1,1],
        [1,1,1,1,1,1]]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx >=n or ny<0 or ny >=m:
                continue
            if graph[nx][ny] ==0:
                continue
            if graph[nx][ny] ==1:
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx, ny))
            print(x,y)
            print(nx,ny)
            print(queue)
            for i in graph:
                print(i)
            print('#'*10)

    return graph

print(bfs(0,0))
'''
5 6
[[1,0,1,0,1,0],
[1,1,1,1,1,1],
[0,0,0,0,0,1],
[1,1,1,1,1,1],
[1,1,1,1,1,1]]
[[3, 0, 5, 0, 7, 0], 
[2, 3, 4, 5, 6, 7], 
[0, 0, 0, 0, 0, 8], 
[14, 13, 12, 11, 10, 9], 
[15, 14, 13, 12, 11, 10]]

'''