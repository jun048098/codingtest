# from math import gcd
# def solution(arr):
#     answer = arr[0]
#     for i in arr:
#         answer = answer * i // gcd(answer, i)
#     return answer


import numpy as np
def solution(arr):
    arr = np.array(arr)
    arr = np.sort(arr)
    n=1
    for i in range(len(arr)):
        n*= arr[i]
        if i < len(arr)-1:
            cnt = 0
            for j in range(i, len(arr)):
                if arr[j]%arr[i] != 0:
                    break
                cnt+=1
            if cnt == len(arr)-i:
                arr //= arr[i]
    return n

print(solution([2,6,8,14]))
