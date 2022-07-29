# def solution(left, right):
#     num_list = [i for i in range(left, right + 1)]
#     d = []  # 약수개수
#
#     for i in num_list:
#         cnt = []
#         for j in range(1, i + 1):
#             if i % j == 0:
#                 cnt.append(j)
#         d.append(len(cnt))
#     #
#     for i in range(len(d)):
#         if d[i] % 2 == 1:
#             num_list[i] = num_list[i] * (-1)
#     answer = sum(num_list)
#
#     return answer

def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer
print(solution(24,	27))