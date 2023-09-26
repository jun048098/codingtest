import sys
import heapq

input = sys.stdin.readline
inf =float('inf')
# 1에서 n번 정점 최단 거리
# 임의의 두 정점 통과
n, e = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

u, v = map(int, input().split())


def dijkstra(start):
    distance = [inf] * (n + 1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for next, cost in graph[now]:
            next_cost = dist + cost
            if next_cost < distance[next]:
                distance[next] = next_cost
                heapq.heappush(q,(next_cost, next))

    return distance

original_dist = dijkstra(1)
u_dist = dijkstra(u)
v_dist = dijkstra(v)

uv_dist = original_dist[u] + u_dist[v] + v_dist[n]
vu_dist = original_dist[v] + v_dist[u] + u_dist[n]

answer = min(uv_dist, vu_dist)
print(answer if answer < inf else -1)