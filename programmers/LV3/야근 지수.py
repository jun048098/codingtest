import heapq
def solution(n, works):
    if sum(works) <= n: return 0
    q = [-w for w in works]
    heapq.heapify(q)

    for _ in range(n):
        i = heapq.heappop(q)
        i += 1
        heapq.heappush(q, i)

    return sum([w ** 2 for w in q])

w = [1,1]
n = 4
print(solution(n, w))