numbers = [1,2,3,4,6,7,8,0]
# answer = 0
# for i in range(10):
#         if i in numbers:
#             print(i)
#         else:
#             answer += i
# print(answer)

def solution(n):
    return sum([i for i in range(10) if i not in n])