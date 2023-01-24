from collections import Counter
# def solution(weights):
#     answer = 0
#     cnt = Counter(weights)
#     for w, v in cnt.items():
#         if  v > 1:
#             answer +=1
#             cnt[w] = 1
#     for w in set(weights):
#         for i in range(2,5):
#             if w * i in cnt:
#                 cnt[w * i] += 1
#             else:
#                 cnt[w * i] = 1
#
#     for v in cnt.values():
#         if v > 1:
#             answer += (v * (v - 1)) //2
#     return answer, cnt


def solution(weights):
    answer = 0
    d = dict()
    for k, v in Counter(weights).items():
        if v > 1:
            answer += 1
        for i in range(2,5):
            if  k*i in d:
                d[k*i] += 1
            else:
                d[k*i] = 1
    for v in d.values():
        if v > 1:
            answer += v  // 2

    return answer


w = [100,180,360,100,270]
# w= [100, 150, 200, 300, 400]
print(solution(w))

