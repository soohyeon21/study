# 11145

# ipt.strip()이 ''로 빈 문자열인 경우를 생각해야 한다.

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    ipt = sys.stdin.readline().strip()
    state = True
    for letter in ipt:
        if (not letter.isdigit()):
            state = False
##    try:
##        tmp = int(ipt)
##    except:
##        state = False
    if (ipt == ''):
        state = False
    
    if (state):
        print(int(ipt))
    else:
        print('invalid input'
