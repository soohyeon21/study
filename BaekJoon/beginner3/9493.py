# 9493

import sys

while (1):
    case = list(map(int, sys.stdin.readline().split()))
    if (case == [0, 0, 0]):
        break

    train = case[0]/case[1]
    plane = case[0]/case[2]
    time = round(abs(train - plane)*3600)

    print("%d:%02d:%02d" %(time//3600, (time%3600)//60, time%60))
