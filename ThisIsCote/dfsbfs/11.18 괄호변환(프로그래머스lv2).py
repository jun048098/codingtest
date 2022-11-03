def check_same(p):
    a=0
    for i in p:
        if i == '(':
            a -= 1
        else:
            a += 1
    if a == 0:
        return True
    else:
        return False

# def check_collect(p):
#     count = 0
#     for i in p:
#         if i == '(':
#             count += 1
#         else:
#             if count == 0:  # count가 0인 된 상태에서 )가 먼저 나오면 쌍 안맞음!
#                 return False
#             count -= 1
#     return True

def check_collect(p):
    a = 0
    for i in p:
        if i == ')':
            a -= 0
            if a <=0:
                return False
        else:
            a += 1
    if a == 0:
        return True
    else:
        return False
def solution(p):
    #step1
    if len(p) == 0 or check_collect(p):
        return p
    #step2
    a = 0
    u = ''
    v = ''
    for i in range(len(p)):
        if p[i] == ')':
            a -= 1
        else:
            a += 1
        if a == 0:
            u = p[:i+1]
            v = p[i+1:]
            break
    #step3
    if check_collect(u) == True:
        #step3-1
        new_v = solution(v)
        return u + new_v
    #step4
    else:
        #step4-1
        answer  = '('
        # step4-2
        new_v = solution(v)
        #step4-3
        answer += new_v +')'
        # step 4-4 ???
        new_u = u[1:-1]
        rev_u = ''
        for i in new_u:
            if i =='(':
                rev_u +=')'
            else:
                rev_u += '('
        answer += rev_u
    return answer

# p = "(()())()"
p ="()))((()"
# p=')('
print(solution(p))
#
# def check_same(p):
#     a=0
#     for i in p:
#         if i == '(':
#             a -= 1
#         else:
#             a += 1
#     if a == 0:
#         return True
#     else:
#         return False
#
# def check_collect(p):
#     a = 0
#     for i in p:
#         if i == ')':
#             a -= 0
#             if a <0:
#                 return False
#         else:
#             a += 1
#     if a == 0:
#         return True
#     else:
#         return False
#
# def solution(p):
#     #step1
#     if len(p) == 0:
#         return ''
#     #step2
#     a = 0
#     for i in range(len(p)):
#         if p[i] == ')':
#             a -= 1
#         else:
#             a += 1
#         if a == 0:
#             u = p[:i+1]
#             v = p[i:]
#             break
#     #step3
#     if check_collect(u) == True:
#         #step3-1
#         new_v = solution(v)
#         return u + new_v
#     #step4
#     else:
#         #step4-1
#         answer  = '('
#         # step4-2
#         new_v = solution(v)
#         #step4-3
#         answer += new_v +')'
#         # step 4-4 ???
#         new_u = u[1:-1]
#         rev_u = ''
#         for i in new_u:
#             if i =='(':
#                 rev_u +=')'
#             else:
#                 rev_u += '('
#         answer += rev_u
#     return answer