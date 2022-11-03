import sys
import heapq
input = sys.stdin.readline
n = int(input())
h = []
for _ in range(n):
    heapq.heappush(h, int(input()))

answer = 0
while len(h) != 1:
    a = heapq.heappop(h)
    b = heapq.heappop(h)
    now = a+b
    answer += now
    heapq.heappush(h, now)
print(answer)