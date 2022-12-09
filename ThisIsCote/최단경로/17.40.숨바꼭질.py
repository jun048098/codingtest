import sys
import heapq
input = sys.stdin.readline
n, m = map(int, input().split())
inf = float('inf')
start = 1
distance = [inf for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b,1))
    graph[b].append((a,1))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

max_node = 0
max_distace = 0
result = []

for i in range(1, n+1):
    if max_distace < distance[i]:
        max_node = i
        max_distace = distance[i]
        result = [max_node]
    elif max_distace == distance[i]:
        result.append(i)

print(max_node, max_distace ,len(result))

'''
6 7
3 6
4 3
3 2
1 3
1 2
2 4
5 2
'''