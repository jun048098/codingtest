from collections import deque
import sys
input = sys.stdin.readline
# n:도시수, m:도로수, k:최단거리, x:출발
n, m, k, x = map(int, input().split())
distance= [-1] * (n+1)
distance[x] = 0
graph =[[] for _ in range(n+1)]
for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)

queue = deque([x])
while queue:
    now = queue.popleft()
    for next in graph[now]:
        if distance[next] ==-1:
            distance[next] = distance[now]+1
            queue.append(next)
check =False
for i in range(1,n+1):
    if k == distance[i]:
        print(i)
        check =True
if check ==False:
    print(-1)
