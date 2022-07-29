absolutes = 	[1, 2, 3]
signs = ['false','false','true']
def solution(absolutes, signs):

    for i in range(len(absolutes)):
        if signs[i] == False:
            absolutes[i] = absolutes[i] * -1
    answer = sum(absolutes)
    return answer

