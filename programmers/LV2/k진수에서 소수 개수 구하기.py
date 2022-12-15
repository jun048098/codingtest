def convert(n, k):
    if k == 10:
        return str(n)
    r = ''
    while n > 0:
        n, mod = divmod(n, k)
        r += str(mod)
    return r[::-1]

def prime(n):
    if n ==1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    convert_n = convert(n,k)
    n_dict = {}
    for i in convert_n.split('0'):
        if i == '':
            continue
        a = int(i)
        if a in n_dict:
            n_dict[a] +=1
        else:
            n_dict[a] = 1
    for i in n_dict:
        if prime(i) == True:
            answer += n_dict[i]
    return answer


print(solution(110011,	10))
print(solution(437674,3))
'''
1. n을 k진수로 바꾸기
2. 0으로 분리하고 딕셔너리로 갯수 세기
3.호출해서 소수 판별

함수
1. 진수 변환
2. 소수 판별
'''
