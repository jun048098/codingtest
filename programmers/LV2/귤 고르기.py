from collections import Counter
# def solution(k, tangerine):
#
#     c = Counter(tangerine)
#     a = 0
#     answer = 0
#     c = sorted([(j,i) for i, j in c.items()], reverse=True)
#     for m , s in c:
#         if a >= k:
#             break
#         a += m
#         answer +=1
#     return answer

# 개선
def solution(k, tangerine):
    answer = 0
    cnt = Counter(tangerine)

    for v in sorted(cnt.values(), reverse=True):
        k-=v
        answer += 1
        if k <= 0 :
            break
    return answer


k = 6
t =	[1, 3, 2, 5, 4, 5, 2, 3]

print(solution(k, t))