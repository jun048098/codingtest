n = int(input())
n_list = [0 for _ in range(n+1)]

for i in range(2, n+1):
    x = []
    if i % 5 ==0:
        x.append(n_list[i // 5]+1)
    if i % 3 == 0:
        x.append(n_list[i // 3]+1)
    if i % 2 == 0:
        x.append(n_list[i // 2]+1)
    x.append(n_list[i-1]+1)
    n_list[i] = min(x)

print(n_list[-1])

# n = int(input())
# d = [0 for _ in range(n+1)]
#
# for i in range(2, n+1):
#     d[i] = d[i-1] + 1
#     if i % 2 ==0:
#         d[i] = min(d[i], d[i//2]+1)
#     if i % 3 == 0:
#         d[i] = min(d[i], d[i//3]+1)
#     if i % 5 == 0:
#         d[i] = min(d[i], d[i//5]+1)
#
#
# print(d[-1])