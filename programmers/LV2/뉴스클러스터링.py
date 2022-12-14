from collections import Counter

def solution(str1, str2):
    s1 = [str1[i-1:i+1].lower() for i in range(1, len(str1)) if str1[i-1:i+1].isalpha()]
    s2 = [str2[i-1:i+1].lower() for i in range(1, len(str2)) if str2[i-1:i+1].isalpha()]
    # 교집합
    inter = sum((Counter(s1) & Counter(s2)).values())
    # 합집합
    union = sum((Counter(s1) | Counter(s2)).values())
    answer = 1 if union == 0 else inter / union
    return int(answer * 65536)


s1  = 'FRANCE'
s2 = 'french'
# s1 = 'handshake'
# s2 = 'shake hands'
s1 = 'aa1+aa2'
s2 = 'AAAA12'
print(solution(s1, s2))
