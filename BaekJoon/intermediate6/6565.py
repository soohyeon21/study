# 6565

# 각 항을 뒤집어서 계산한 결과가 식의 결과값을 뒤집은 값과 같다면 True, 다르면 False

import sys

while (1):
    equa = sys.stdin.readline().rstrip()
    if (equa == "0+0=0"):
        print("True")
        break

    left, right = equa.split("=")
    term1, term2 = left.split("+")
    if (int(term1[::-1]) + int(term2[::-1]) == int(right[::-1])):
        print("True")
    else:
        print("False")
