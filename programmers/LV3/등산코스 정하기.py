# 다익스트라
import heapq
def dijkstra(start, n, gates, summits, graph, answer):
    inf = float('inf')
    q = []
    heapq.heappush(q, (0, start))
    visited = [False] * (n+1)
    while q:
        inten, node = heapq.heappop(q)

        for i, nxd in graph[node]:
            if nxd in gates :
                continue



def solution(n, paths, gates, summits):
    inf = float('inf')
    answer = [inf, inf]
    graph = [[] for _ in range(n+1)]
    for x, y, i in paths:
        graph[x].append((i, y))
        graph[y].append((i, x))

    for g in gates:
        dijkstra(g, n ,gates, summits, graph, answer)


    return answer