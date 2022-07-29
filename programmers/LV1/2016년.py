def solution(a, b):
    cale = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    sum_date = 0
    for i in range(a-1):
        sum_date += cale[i]

    d = sum_date % 7

    answer = day[d]
    return answer

print(solution(6,1))