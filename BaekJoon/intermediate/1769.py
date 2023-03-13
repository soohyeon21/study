# 1769

# mul3 대신 (number % 3 == 0) 조건 사용해도 된다.

import sys

x = sys.stdin.readline().rstrip()
course = 0
mul3 = ["3", "6", "9"]

while (len(x) != 1):
    x = str(sum(int(digit) for digit in x))
    course += 1

print(course)
if (x in mul3):
    print("YES")
else:
    print("NO")
