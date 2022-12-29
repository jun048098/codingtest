from itertools import combinations
from collections import Counter
# def solution(orders, course):
#     answer = []
#     new_s = [set(i) for i in orders]
#     o = sorted(set(''.join(orders)))
#     for c in course:
#         cnt = []
#         for o in orders:
#             for com in combinations(o, c):
#                 cmb = ''.join(sorted(com))
#                 cnt.append(cmb)
#
#         s = Counter(cnt)
#         if len(s) == 0:
#             continue
#         m = max(s.values())
#         for k, v in s.items():
#             if m == v and v > 1:
#                 answer.append(k)
#     return sorted(answer)

from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    for c in course:
        cnt = []
        for o in orders:
            for com in combinations(o, c):
                cmb = ''.join(sorted(com))
                cnt.append(cmb)

        s = Counter(cnt).most_common()
        answer += [o for o, c in s if c > 1 and c == s[0][1] ]
    return sorted(answer)


# print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],	[2,3,4]))
# print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],	[2,3,5]))
print(solution(["XYZ", "XWY", "WXA"]	,[2,3,4]))
'''
코스 한개씩 호출
    i 가 c 개보다 길면
        j가 c보다 길면
            i j 교집합을 리스트에 추가


리스트 counter
max 호출

'''


