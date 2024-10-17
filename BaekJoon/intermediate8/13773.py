# 13773

import sys

while (1):
    year = int(sys.stdin.readline())
    if (year == 0):
        break

    state = "No summer games"
    if (year % 4 == 0):
        if ((year in range(1914, 1919)) or (year in range(1939, 1946))):
            state = "Games cancelled"
        elif (year > 2020):
            state = "No city yet chosen"
        elif (year < 1896):
            pass
        else:
            state = "Summer Olympics"

    print(f"{year} {state}")
