# def solution(n, left, right):
#     answer = []
#     for i in range(left, right+1):
#         x = i // n
#         y = i % n
#         if x >= y:
#             answer.append(x+1)
#         else:
#             answer.append(y+1)
#
#     return answer

def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        answer.append(max(i//n, i%n) +1 )
    return answer

n, l, r = 3, 2,	5
n, l,r = 4,	7,	14
print(solution(n,l,r))