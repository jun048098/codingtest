# 실패
n, m = map(int, input().split())
w = list(map(int, input().split()))
array = [0]*11
for i in w:
    array[i] += 1

answer = 0

for i in range(1, m+1):
    # a 선택 중복 제거
    n -= array[i]
    # b 선택
    answer += array[i] * n

print(answer)

'''
5 3
1 3 2 3 2
8
'''