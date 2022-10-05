n, m = map(int, input().split())
n_list = [int(input()) for i in range(n)]

m_list = [0] + [10001] * m

for money in n_list:
    for i in range(money, m+1):
        if m_list[i-money] != 10001:
            m_list[i] = min(m_list[i-money] + 1, m_list[i])

if  m_list[-1] == 10001:
    print(-1)
else:
    print(m_list[-1])

'''
2 15
2
3

3 4
3
5
7
'''