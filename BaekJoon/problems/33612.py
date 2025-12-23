# 33612

# year를 모두 month로 고치고, month%12==0인지에 따라 처리하는 방법도 있음.

import sys

n = int(sys.stdin.readline())

month = 8 + (n-1)*7
year = 2024 + month//12
month %= 12
if (month == 0):
    month = 12
    year -= 1

print(year, month)
