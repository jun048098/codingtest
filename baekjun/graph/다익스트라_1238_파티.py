import sys
import heapq
#개선 코드 reverse graph
input = sys.stdin.readline
inf = float('inf')
# n학생, m도로 수, x 타겟
n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
reverse_graph = [[] for _ in range(n+1)]

for _ in range(m):
    s, e, t = map(int, input().split())
    graph[s].append((e, t))
    reverse_graph[e].append((s,t))

def dijkstra(start, use_graph):
    distance = [inf for _ in range(n + 1)]
    q = []
    heapq.heappush(q,(0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for end, time in use_graph[now]:
            cost = time + dist
            if cost < distance[end]:
                distance[end] =cost
                heapq.heappush(q, (cost, end))
    return distance

answer = 0
go = dijkstra(x, reverse_graph)
back = dijkstra(x, graph)
for i in range(1, n+1):
    answer = max(answer, go[i]+back[i])

print(answer)

#
# input = sys.stdin.readline
# inf = float('inf')
# # n학생, m도로 수, x 타겟
# n, m, x = map(int, input().split())
# graph = [[] for _ in range(n+1)]
#
# for _ in range(m):
#     s, e, t = map(int, input().split())
#     graph[s].append((e, t))
#
# def dijkstra(start):
#     distance = [inf for _ in range(n + 1)]
#     q = []
#     heapq.heappush(q,(0, start))
#     distance[start] = 0
#     while q:
#         dist, now = heapq.heappop(q)
#         if distance[now] < dist:
#             continue
#
#         for end, time in graph[now]:
#             cost = time + dist
#             if cost < distance[end]:
#                 distance[end] =cost
#                 heapq.heappush(q, (cost, end))
#     return distance
#
# answer = 0
# back = dijkstra(x)
# for i in range(1, n+1):
#     go = dijkstra(i)[x]
#     answer = max(answer, go + back[i])
#
# print(answer)

