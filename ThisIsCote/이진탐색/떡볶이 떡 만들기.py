n, m = map(int, input().split())
h = list(map(int,input().split()))
start = 0
end = max(h)
result = 0

while start <= end:
    cut = 0
    mid = (start + end) // 2
    for i in h:
        if i > mid:
            # 잘린 떡
            cut += i - mid
    # 부족한 경우
    if cut < m:
        end = mid - 1

    else:
        result = mid
        start = mid + 1

print(result)
'''
4 6
19 15 10 17
'''