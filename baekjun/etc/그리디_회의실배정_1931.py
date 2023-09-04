import sys
input = sys.stdin.readline


n = int(input())

room = []
for i in range(n):
    time = list(map(int, input().split()))
    room.append(time)

room.sort(key= lambda x: (x[1], x[0]))

answer = 1
last = room[0][1]
for i in range(1, n):
    if last <= room[i][0]:
        answer += 1
        last = room[i][1]

print(answer)

