import re
s = input()
new_s = re.sub('1+', '1', s)
new_s = re.sub('0+', '0', new_s)

if new_s.count('0') > new_s.count('1'):
    print(new_s.count('1'))
else:
    print(new_s.count('0'))

'''
0001100
'''

