def solution(num):
    cnt = 0
    while num != 1:
        if num % 2 == 0:
            num /= 2

        else:
            num = num * 3 + 1

        cnt += 1

        if cnt == 500:
            cnt = -1
            break

    return cnt

a = 't t'
a= a.upper()
print(a)