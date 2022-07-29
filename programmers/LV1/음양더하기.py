absolutes = 	[1, 2, 3]
signs = [False, False, True]
# def solution(absolutes, signs):
#
#     for i in range(len(absolutes)):
#         if signs[i] == False:
#             absolutes[i] = absolutes[i] * -1
#     answer = sum(absolutes)
#     return answer


def solution(a,s):
    return sum([i if j else -i  for i, j in zip(a,s) ])
print(solution(absolutes,signs ))