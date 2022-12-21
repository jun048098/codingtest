def solution(numbers):
    answer = []
    for n in numbers:
        k = list('0' + bin(n)[2:])
        idx = ''.join(k).rfind('0')
        k[idx] = '1'
        if n % 2 == 1:
            k[idx+1] = '0'
        answer.append(int(''.join(k),2))
    return answer

print(solution([2,7]))


