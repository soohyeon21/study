# 6825

# 첫 if에서 25 초과 거르고 나면, 두번째 elif에서는 18.5 이상만 조건으로 넣어도 된다.

import sys

weight = float(sys.stdin.readline())
height = float(sys.stdin.readline())

bmi = weight/height**2

state = ""
if (bmi > 25):
    state = "Overweight"
elif (18.5 <= bmi <= 25):
    state = "Normal weight"
else:
    state = "Underweight"

print(state)
