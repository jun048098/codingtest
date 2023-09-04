# import heapq
#
# def solution(s):
#     h = heapq()
#     for o in s:
#         if o == 'D 1':
#             if h:
#
#
#         elif o == 'D -1':
#             if h:
#                 heapq.heappop(h)
#         else:
#             heapq.heappush(h, int(o[2:]))
#
#     if not h:
#         return [0,0]
#
#     return


# def solution(s):
#     q = []
#     for i in s:
#         if i[0] == 'I':
#             q.append(int(i[2:]))
#         elif i == 'D -1':
#             if len(q) > 0:
#                 q.remove(min(q))
#         else:
#             if len(q) > 0:
#                 q.remove(max(q))
#
#     if q == []:
#         return [0, 0]
#     else:
#         return [max(q), min(q)]