# 5074

import sys

while (1):
    start, duration = sys.stdin.readline().split()
    if ((start == "00:00") and (duration == "00:00")):
        break

    start = list(map(int, start.split(":")))
    duration = list(map(int, duration.split(":")))
    total = start[0]*60 + start[1] + duration[0]*60 + duration[1]
    
    days = 0
    if (total >= 24*60):
        days = total // (24*60)
        total %= 24*60
        
    print(f"{total//60:02}:{total%60:02}", end="")
    if (days):
        print(f" +{days}")
    else:
        print()
