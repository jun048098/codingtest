# bfs
from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
start, target = map(int,input().split())
e = int(input())
graph =[[] for _ in range(n+1)]
for i in range(e):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visit = [-1] *(n+1)
visit[start] = 0
q = deque([start])
while q:
    s = q.popleft()
    for i in graph[s]:
        if visit[i] ==-1:
            visit[i] = visit[s]+1
            q.append(i)
print(visit[target])