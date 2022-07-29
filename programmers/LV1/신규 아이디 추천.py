import re

def solution(new_id):
    st = new_id
    # 1
    st = st.lower()
    #2
    st = re.sub('[^a-z0-9\-_.]', '', st)
    #3
    st = re.sub('\.+', '.', st)
    #4
    st = re.sub('^[.]|[.]$', '', st)
    #5
    st = 'a' if len(st) == 0 else st[:15]
    #6
    st = re.sub('^[.]|[.]$', '', st)
    #7
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st
print(solution("...!@BaT#*..y.abcdefghijklm"))

# def solution(new_id):
#     # Lv1
#     new_id_1 = new_id.lower()
#
#     # Lv2
#     collect = 'abcdefghijklmnopqrstuvwxyz-_.0123456789'
#     for i in new_id_1:
#         if i not in collect:
#             new_id_1 = new_id_1.replace(i, '')
#
#     # Lv3
#     lv3 = new_id_1[0]
#     for i in range(1, len(new_id_1)):
#
#         if new_id_1[i] == '.' and lv3[-1] == '.':
#             continue
#         else:
#             lv3 += new_id_1[i]
#
#     return lv3
#
# print(solution("...!@BaT#*..y.abcdefghijklm"))