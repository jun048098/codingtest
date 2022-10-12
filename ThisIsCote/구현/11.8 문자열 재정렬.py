s = input()
alp = []
num = 0

for i in s:
    if i.isalpha() == True:
        alp.append(i)
    else:
        num += int(i)

alp.sort()
if num != 0:
    alp.append(str(num))


print(''.join(alp))
'''
K1KA5CB7
'''