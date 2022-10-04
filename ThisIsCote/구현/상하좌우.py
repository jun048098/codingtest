n = int(input())
order = input().split()
direction = {'L':(0,-1), 'R':(0,1), 'U':(-1,0), 'D':(1,0)}
x,y = 1, 1

for i in order:
    nx = x + direction[i][0]
    ny = y + direction[i][1]
    if nx >= 1 and ny >= 1 and nx<=n and ny<=n:
        x, y =nx, ny


print(x,y)

'''
5
R R R U D D
'''