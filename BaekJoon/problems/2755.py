# 2755

# int(earned/total*100 + 0.5)/100 하는 방법도 있다.

import sys

n = int(sys.stdin.readline())

total = 0
earned = 0
change = {'A+':4.3, 'A0':4, 'A-':3.7, 'B+':3.3, 'B0':3, 'B-':2.7, 'C+':2.3, 'C0':2, 'C-':1.7, 'D+':1.3, 'D0':1, 'D-':0.7, 'F':0}
for _ in range(n):
    sclass, score, grade = sys.stdin.readline().split()
    total += int(score)
    earned += int(score)*change[grade]

second = int(earned/total*100)/100
third = earned/total*1000%10
if (third > 4):
    second += 0.01

print(f"{second:.2f}")
