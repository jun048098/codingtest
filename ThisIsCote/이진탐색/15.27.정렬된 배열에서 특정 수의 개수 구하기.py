n, target = map(int, input().split())
array = list(map(int, input().split()))

def count_value(array, target):
    a = first(array, target, 0, n-1)
    if a == None:
        return -1
    b = last(array, target, 0, n-1)
    return b-a+1

def first(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    #
    if (mid == 0 or target > array[mid-1]) and target == array[mid]:
        return mid
    elif target <= array[mid]:
        return first(array, target, start, mid-1)
    else:
        return first(array, target, mid+1, end)

def last(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) //2
    if (mid == n-1 or target < array[mid+1]) and target  == array[mid]:
        return mid
    elif target >= array[mid]:
        return last(array, target, mid+1, end)
    else:
        return last(array, target, start, mid-1)

print(count_value(array, target))

'''
7 2
1 1 2 2 2 2 3
7 4
1 1 2 2 2 2 3
'''