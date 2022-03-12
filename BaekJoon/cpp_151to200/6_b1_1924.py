# 1924

# cnt % 7은 한번만 계산해서 rst에 넣고, 그럼 값이 0~6사이에 나올 테니
# date = ["SUN", "MON", ..., "SAT"]만들어서 date[rst] 해도 되겠다!!

import sys

m, d = map(int, sys.stdin.readline().split())
year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

cnt = 0
for i in range(m-1):
    cnt += year[i]
cnt += d

if (cnt % 7 == 0):
    print("SUN")
elif (cnt % 7 == 1):
    print("MON")
elif (cnt % 7 == 2):
    print("TUE")
elif (cnt % 7 == 3):
    print("WED")
elif (cnt % 7 == 4):
    print("THU")
elif (cnt % 7 == 5):
    print("FRI")
elif (cnt % 7 == 6):
    print("SAT")
