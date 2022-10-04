n, m, k = map(int, input().split())
num = list(map(int, input().split()))

num.sort(reverse= True)
def solution1(n,m,k,num):
    num_sum = 0
    cnt = 0
    num_count =0

    while cnt != m:
        cnt += 1
        num_count += 1
        if num_count == k+1:
            num_sum += num[1]
            num_count = 0
        else:
            num_sum += num[0]
    return num_sum

def solution2(n,m,k,num):
    a = num[0] * k + num[1]
    a *= m // (k+1)
    a += (m % (k+1)) * num[0]
    return a
print(solution1(n,m,k,num))
print(solution2(n,m,k,num))
'''
5 8 3
2 4 5 4 6
'''