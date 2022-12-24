def solution(number, k):
    a=[]
    for n in number:
        while a and a[-1] < n:
            if k==0:
                break
            a.pop()
            k-=1
        a.append(n)
    for _ in range(k):
        a.pop()
    return ''.join(a)

print(solution("4177252841",4))
