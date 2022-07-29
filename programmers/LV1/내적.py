a =[-1,0,1]
b = [1,0,-1]
# import numpy as np
# def solution(a,b):
#     return sum((np.array(a) * np.array(b)).tolist())

def solution(a,b):
    return sum([i*j for i,j in zip(a,b)])
print(solution(a,b))