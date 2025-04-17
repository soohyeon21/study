# 1267

import sys

n = int(sys.stdin.readline())
calls = list(map(int, sys.stdin.readline().split()))

young = 0
mins = 0
for call in calls:
    young += (call//30+1)*10
    mins += (call//60+1)*15

if (young < mins):
    print(f"Y {young}")
elif (young > mins):
    print(f"M {mins}")
elif (young == mins):
    print(f"Y M {young}")
