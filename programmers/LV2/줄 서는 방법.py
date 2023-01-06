# 효율성 실패
# from itertools import permutations
# def solution(n, k):
#     a = [i for i in range(1, n+1)]
#     b = [i for i in permutations(a,n)]
#     return b[k-1]

import math


def solution(n, k):
    k -= 1
    answer = []
    num = [i for i in range(1, n+1)]
    while num:
        n -= 1
        f = math.factorial(n)
        answer.append(num.pop(k // f))
        k = k % f
    return answer

print(solution(3	,5))
'''
팩토리아 구하기

n//k  
'''