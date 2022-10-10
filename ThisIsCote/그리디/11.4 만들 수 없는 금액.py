# 실패 문제

n = int(input())
m = list(map(int, input().split()))
m.sort()

target = 1
for x in m:
    if target < x:
        break
    target += x

print(target)

'''
5
3 2 1 1 9
'''
