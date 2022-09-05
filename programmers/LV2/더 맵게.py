# # 시간 초과
# def solution(scoville, K):
#     cnt = 0
#     while min(scoville) < K:
#         new = []
#         for i in range(2):
#             new.append(min(scoville))
#             scoville.remove(min(scoville))
#         scoville.append(min(new) + (2 * max(new)))
#         cnt += 1
#
#         if len(scoville) <= 2 and min(scoville) < K:
#             # break
#             return -1
#
#     return cnt
import heapq
def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)
    while scoville[0] < K and len(scoville) >1:
        s1 = heapq.heappop(scoville)
        s2 = heapq.heappop(scoville)
        heapq.heappush(scoville, s1 +s2*2)
        cnt+=1

    return cnt if scoville[0] > K else -1