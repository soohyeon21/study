# 9228

# "If it is equal to 11, the digit 0 is appended as the check digit,
# and if it is equal to 10, then the original number is rejected."

import sys

while (1):
    original = sys.stdin.readline().rstrip()
    if (original == "#"):
        break

    mul = 2
    total = 0
    for digit in original[::-1]:
        total += int(digit)*mul
        mul += 1
    check = 11 - total%11 # or ((11-total%11)%11)

    print(f"{original} -> ", end="")
    if (check == 10):
        print("Rejected")
    elif (check == 11):
        print(0)
    else:
        print(check)
