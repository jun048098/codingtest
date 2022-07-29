# def solution(n, arr1, arr2):
#     wall = {1:'#', 0:' '}
#     arr1_2 = [ '0'*(n-len(bin(i)[2:])) + bin(i)[2:] for i in arr1]
#     arr2_2 = ['0'*(n-len(bin(i)[2:])) + bin(i)[2:] for i in arr2]
#     answer = [  ]
#     for i, j in zip(arr1_2, arr2_2):
#         new_map =''
#         for k in range(n):
#             if i[k]== '0' and j[k] == '0':
#                 new_map += ' '
#             else:
#                 new_map+= '#'
#         answer.append(new_map)
#     return answer


def solution(n, arr1, arr2):
    answer = []
    for i, j  in zip(arr1, arr2):
        a12 = bin(i|j)[2:]
        a12 = a12.rjust(n,'0')
        a12 = a12.replace('0', ' ')
        a12 = a12.replace('1', '#')
        answer.append(a12)
    return answer