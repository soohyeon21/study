# 1942

import sys

for _ in range(3):
    start, end = sys.stdin.readline().split()
    start = list(map(int, start.split(":")))
    end = list(map(int, end.split(":")))
    now = start
    end_sec = end[0]*3600 + end[1]*60 + end[2]
    
    cnt = 0

    while (1):
        num = int(str(now[0])+str(now[1])+str(now[2]))
        if (num%3 == 0):
            cnt += 1

        sec = now[0]*3600+now[1]*60+now[2] + 1
        now[0], now[1], now[2] = sec//3600%24, sec//60%60, sec%60
        
        if ((now[0] == (end_sec+1)//3600%24) and (now[1] == (end_sec+1)//60%60) and (now[2] == (end_sec+1)%60)):
            print(cnt)
            break
