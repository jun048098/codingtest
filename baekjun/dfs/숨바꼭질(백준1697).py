# https://www.acmicpc.net/problem/1697
from collections import deque

def bfs(x, y):
    max_num = 10**5
    dist = [0] * (max_num +1)
    q = deque()
    q.append(x)
    while q:
        nx = q.popleft()
        if nx == y:
            print(dist[nx])
            break
        for n in (nx-1, nx + 1, nx * 2):
            if n >= 0 and n <= max_num and not dist[n]:
                dist[n] = dist[nx] +1
                q.append(n)


x, y = map(int, input().split())
bfs(x, y)
