participant= ["mislav", "stanko", "mislav", "ana"]
completion=["stanko", "ana", "mislav"]
# def s(p,c):
#     p.sort()
#     c.sort()
#     for i in range(len(c)):
#         if c[i] != p[i]:
#             return p[i]
#     return p[-1]
# print(s(participant, completion))

import collections
def solution(p,c):
    a = collections.Counter(p) - collections.Counter(c)
    return  list(a.keys())[0]
print(solution(participant, completion))