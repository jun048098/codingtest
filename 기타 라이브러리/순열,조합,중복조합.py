from itertools import combinations
from itertools import combinations_with_replacement
from itertools import permutations
from itertools import product

dic = ['a', 'b','c','d']

# 조합
# nCr   n!/(n-r)!r!
# 순서에 상관없이 뽑기
com_d = list(combinations(dic, len(dic)))
print('com:', com_d)

# 중복 조합
# nHr   n+r-1Cr
# com_r_d = list(combinations_with_replacement(dic,len(dic)))
com_r_d = list(combinations_with_replacement(dic,2))
print('com_r:', com_r_d)


# 순열
# nPr   n!/(n-r)!
# 순서상관 있음
per_d = list(permutations(dic, len(dic)))
print('per:', per_d)

# 중복순열
# nPIr n^r
pro_d = list(product(dic, repeat = len(dic)))
# print('pro', pro_d)
print(len(pro_d))

num = [1,2,3,4]
abc = ['a','b','c']
pro_two_list = list(product(num, abc, repeat=2))
print('pro_two_list: ', pro_two_list)