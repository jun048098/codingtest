n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))
def binary_search(array, target, start, end):
    while start<=end:
        mid = (start+ end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid-1
    return None

n_list.sort()
answer = ''
for i in m_list:
    if binary_search(n_list, i, 0, n-1) == None:
        answer += 'no '
    else:
        answer += 'yes '

print(answer.rstrip())
'''
5 
8 3 7 9 2
3
5 7 9
'''