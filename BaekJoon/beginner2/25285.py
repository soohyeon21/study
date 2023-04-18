# 25285

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    cm, kg = map(int, sys.stdin.readline().split())
    lev = 0
    bmi = kg/(cm*0.01)**2
    
    if (cm < 140.1):
        lev = 6
    elif (140.1 <= cm < 146):
        lev = 5
    elif (146 <= cm < 159):
        lev = 4
    elif (159 <= cm < 161):
        if (16 <= bmi < 35):
            lev = 3
        else:
            lev = 4
    elif (161 <= cm < 204):
        if (20 <= bmi < 25):
            lev = 1
        elif ((18.5 <= bmi < 20) or (25 <= bmi < 30)):
            lev = 2
        elif ((16 <= bmi < 18.5) or (30 <= bmi < 35)):
            lev = 3
        else:
            lev = 4
    else:
        lev = 4

    print(lev)
