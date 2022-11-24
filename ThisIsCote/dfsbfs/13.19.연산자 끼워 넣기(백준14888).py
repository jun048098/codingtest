from itertools import permutations
from collections import deque

n =int(input())
num_list = list(map(int, input().split()))
a = list(map(int, input().split()))
b = ['+', '-', '*', '/']
oper = ''
for i in range(4):
    oper += b[i]*a[i]
oper_list = [i for i in oper]
per_list = deque(permutations(oper_list,  n-1))

# max_num = 10**(-9)
# min_num = 10**9
max_num = -1e9
min_num = 1e9

while per_list:
    total = num_list[0]
    now = per_list.pop()
    for i in range(1, n):
        if now[i-1] == '+':
            total += num_list[i]
        elif now[i-1] == '-':
            total -= num_list[i]
        elif now[i-1] == '*':
            total *= num_list[i]
        elif now[i-1] == '/':
            if total<0:
                total *= -1
                total //= num_list[i]
                total *= -1
            else:
                total //= num_list[i]

    max_num = max(max_num, total)
    min_num = min(min_num, total)

print(max_num)
print(min_num)

# # print(-1e9 == 10**(-9))
# print(-1e9)
# print(10**(-9))
# print()