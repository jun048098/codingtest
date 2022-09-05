import re
def solution(files):
    p = [re.split(r'([0-9]+)',f) for f in files]
    p = sorted(p, key = lambda x: (x[0].lower() ,int(x[1])) )
    p = [''.join(i)for i in p]
    return p
'''
숫자, 공백, ., -
head   문자 1이상
number 숫자 1-5 0-9
tail   문자 숫자 있거나 없거나 

head 사전순 정렬 대소문자 구분 x
대소문자 뺴고 같으면 number 숫자순 앞부분 0은 무시
tail은 원래 순서 유지
'''