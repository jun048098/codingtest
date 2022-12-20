def solution(dirs):
    answer = 0
    a=[]
    dx = 5
    dy = 5
    w = {'U':(-1,0), 'D':(1,0), 'L':(0,-1), 'R':(0,1)}
    for s in dirs:
        nx = w[s][0] + dx
        ny = w[s][1] + dy
        if nx < 0 or ny < 0 or nx >= 11 or ny >= 11:
            continue
        dxny = sorted(((nx, ny), (dx, dy)))
        if dxny not in a:
            answer += 1
            a.append(dxny)
        dx, dy = nx, ny
    return answer


a = "ULURRDLLU"
# a = "LULLLLLLU"
print(solution(a))