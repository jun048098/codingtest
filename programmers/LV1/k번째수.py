def solution(a,c):
    return list(map(lambda x: sorted(a[c[0],c[1]])[c[2]],c))