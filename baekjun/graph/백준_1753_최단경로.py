import sys
import heapq

input = sys.stdin.readline
INF = float('inf')

v, e = map(int, input().split())
start = int(input())

graph = [[] for i in range(v+1)]
distance = [INF] * (v+1)

for i in range(e):
    u, u_v, w  = map(int, input().split())
    graph[u].append((u_v, w))

def dijkstra(start):
    distance[start] = 0 
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist :
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, v+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])