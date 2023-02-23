# 15080

import sys

enter = sys.stdin.readline().split(" : ")
leave = sys.stdin.readline().split(" : ")

entersec = int(enter[0])*3600 + int(enter[1])*60 + int(enter[2])
leavesec = int(leave[0])*3600 + int(leave[1])*60 + int(leave[2])
if (leavesec < entersec):
    leavesec += 24*3600

print(leavesec - entersec)
