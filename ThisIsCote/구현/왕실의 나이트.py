start = input()
# locate_x = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
# x = locate_x[start[0]]
direction = [(-2,-1), (-2,1), (2,-1), (2,1), (-1,-2), (1,-2), (-1,2), (1,2)]
x = int(ord(start[0])) - int(ord('a')) +1
y = int(start[1])

answer = 0
for dx, dy in direction:
    nx = x+dx
    ny = y+dy
    if nx>=1 and ny>=1 and nx<=8 and ny<=8:
        answer +=1
print(answer)

'''a1'''