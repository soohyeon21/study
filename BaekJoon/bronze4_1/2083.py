# 2083

# if 조건문에서 int()하는 방법도 있다.

import sys

while (1):
    name, age, kg = sys.stdin.readline().split()
    if (name == "#"):
        break

    state = ""
    age = int(age)
    kg = int(kg)
    if ((age > 17) or (kg >= 80)):
        state = "Senior"
    else:
        state = "Junior"

    print(name, state)
