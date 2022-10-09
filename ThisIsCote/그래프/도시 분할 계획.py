# 신장트리
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
parent = [i for i in range(n+1)]

edges = [list(map(int, input().split())) for _ in range(m)]
edges.sort(key=lambda x: x[2])
result = 0
last = 0

for edge in edges:
    a, b, cost = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        last = cost

print(result - last)
'''
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4

'''

# edges = []
# for i in range(m):
#     a, b, cost = map(int, input().split())
#     edges.append((cost, a, b))
#
# edges.sort()
# last = 0
#
# for edge in edges:
#     cost, a, b = edge
#     if find_parent(parent, a) != find_parent(parent, b):
#         union_parent(parent, a, b)
#         result += cost
#         last = cost
#
# print(result - last)
