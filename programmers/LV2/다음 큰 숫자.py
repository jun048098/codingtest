def solution(n):
    big =n+1
    while bin(n).count('1')!= bin(big).count('1'):
        big+=1
    return big