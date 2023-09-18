n,k = map(int, input().split())

money = [int(input())for _ in range(n)]
cnt = 0

for i in range(len(money)-1, -1,-1):
    if money[i] <= k:
        quo, k = divmod(k, money[i])
        cnt += quo

print(cnt)