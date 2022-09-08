def solution(s):
    s_list = [int(i) for i in s.split(' ')]
    return str(min(s_list)) + ' ' +str(max(s_list))