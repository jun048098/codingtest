# def solution(s):
#     s_list = list(s)
#     cnt =1
#     for i in range(len(s_list)):
#         if s_list[i] == ' ':
#             cnt = 0

#         if cnt % 2 == 1:
#             s_list[i] =s_list[i].upper()
#         else:
#             s_list[i] =s_list[i].lower()
#         cnt +=1

#     return ''.join(s_list)
# def solution(s):
#     s_list = s.split(' ')
#     new = []
#
#     for i in range(len(s_list)):
#         for j in range(len(s_list[i])):
#             if j % 2 == 0:
#                 new.append(s_list[i][j].upper())
#             else:
#                 new.append(s_list[i][j].lower())
#         new.append(' ')
#     new = ''.join(new)
#
#     return new[:-1]
def solution(s):
    return ' '.join(list(map( lambda x: ''.join( [j.upper() if i %2 ==0 else j.lower() for i, j in enumerate(x)]), s.split(' '))))

print(solution("try hello world"))