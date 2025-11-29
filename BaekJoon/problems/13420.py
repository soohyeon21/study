# 13420

import sys

def cal(equ):
    if (equ[1] == '+'):
        return int(equ[0]) + int(equ[2])
    elif (equ[1] == '-'):
        return int(equ[0]) - int(equ[2])
    elif (equ[1] == '*'):
        return int(equ[0]) * int(equ[2])
    elif (equ[1] == '/'):
        return int(equ[0]) // int(equ[2])


t = int(sys.stdin.readline())
for _ in range(t):
    ipt = sys.stdin.readline().split()

    if (cal(ipt) == int(ipt[-1])):
        print('correct')
    else:
        print('wrong answer')
