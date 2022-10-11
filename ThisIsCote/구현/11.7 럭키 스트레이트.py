n =input()
n = [int(i) for i in n]

if sum(n[:len(n)//2]) == sum(n[len(n)//2:]):
    print('LUCKY')
else:
    print('READY')
'''
123402
 '''