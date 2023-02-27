# 6763

import sys

std = int(sys.stdin.readline())
speed = int(sys.stdin.readline())

fine = 0
if (speed - std <= 0):
    print("Congratulations, you are within the speed limit!")
else:
    if (1 <= speed - std <= 20):
        fine = 100
    elif (21 <= speed - std <= 30):
        fine = 270
    else:
        fine = 500
    print(f"You are speeding and your fine is ${fine}.")
