import heapq
import sys
input = sys.stdin.readline
inf = int(1e9)

# 노드, 간선의 개수
n, m = map(int, input().split())
# 시작 노드
start = int(input())
# 노드 연결 정보
graph = [[] for i in range(n+1)]
# 거리 정보
distance= [inf] * (n+1)
# 간선정보
for _ in range(m):
    a, b, c = map(int,input().split())
    # a번 노드에서 b번 노드로 가는 비용 c
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        # 최단 거리가 가장 짧은 노드 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 노드
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접 노드
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n+1):
    if distance[i] ==inf:
        print('infinity')
    else:
        print(distance[i])

'''
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5 
4 3 3
4 5 1
5 3 1
5 6 2
'''