# 9493

# "초(second)는 반올림하고, 시(hour)는 최소 자리로 나타낸다."

import sys

while (1):
    case = list(map(int, sys.stdin.readline().split()))
    if (case == [0, 0, 0]):
        break

    train = case[0]/case[1]
    plane = case[0]/case[2]
    time = round(abs(train - plane)*3600)

    print(f"{time//3600}:{(time%3600)//60:02}:{time%60:02}")

##    print("%d:%02d:%02d" %(time//3600, (time%3600)//60, time%60))
