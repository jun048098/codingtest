'''
C# H
D# I
F# J
G# K
A# L

'''
#
def solution(m, musicinfos):
    answer= []
    new_m = []
    for i in m:
        if i != "#":
            new_m.append(i)
        else:
            last = new_m.pop()
            if last =='C':
                new_m.append('H')
            elif last =='D':
                new_m.append('I')
            elif last == 'F':
                new_m.append('J')
            elif last == 'G':
                new_m.append('K')
            elif last == 'A':
                new_m.append('L')
    new_m= ''.join(new_m)
    cnt = 0
    for info in musicinfos:
        cnt +=1
        start, end, name, melody = info.split(',')
        time = (60*int(end[:2]) +int(end[3:])) - (60*int(start[:2]) + int(start[3:]))
        melody_list = []
        for i in melody:
            if i != "#":
                melody_list.append(i)
            else:
                last = melody_list.pop()
                if last == 'C':
                    melody_list.append('H')
                elif last == 'D':
                    melody_list.append('I')
                elif last == 'F':
                    melody_list.append('J')
                elif last == 'G':
                    melody_list.append('K')
                elif last == 'A':
                    melody_list.append('L')
        melody_list = melody_list * (time // len(melody_list)) +melody_list[:time % len(melody_list)]
        new_melody = ''.join(melody_list)
        if new_m in new_melody:
            answer.append((cnt, time, name) )
    if len(answer)==0:
        return "(None)"
    else:
        answer= sorted(answer, key= lambda x :( -x[1], x[0]))
        return answer[0][-1]


def solution(m, musicinfos):
    answer= []
    m =m.replace('C#','c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')

    for idx, info in enumerate(musicinfos):
        start, end, name, melody = info.split(',')
        time = (60*int(end[:2]) +int(end[3:])) - (60*int(start[:2]) + int(start[3:]))
        melody = melody.replace('C#','c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')

        melody = melody * (time // len(melody)) +melody[:time % len(melody)]
        new_melody = ''.join(melody)

        if m in new_melody:
            answer.append((idx, time, name) )

    if len(answer)==0:
        return "(None)"
    else:
        answer= sorted(answer, key= lambda x :( -x[1], x[0]))
        return answer[0][-1]


m = "ABCDEFG"
u = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF", "12:00,12:14,HELL,CDEFGAB"]
print(solution(m,u))
m = "CC#BCC#BCC#BCC#B"
u = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
print(solution(m,u))
m = "ABC"
u = ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]
print(solution(m,u))





