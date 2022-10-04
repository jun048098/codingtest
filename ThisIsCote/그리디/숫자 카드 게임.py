n, m = map(int, input().split())
num = [list(map(int, input().split())) for _ in range(m)]
answer = 0
for i in num:
    min_num = min(i)
    answer = max(answer, min_num)

print(answer)
'''
3 3 
3 1 2
4 1 4
2 2 2
'''