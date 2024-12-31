# 26767

# 7과 11의 배수 # Wiwat!
# 7의 배수 # Hurra!
# 11의 배수 # Super!

import sys

n = int(sys.stdin.readline())

for num in range(1, n+1):
    if ((num%7 == 0) and (num%11 == 0)):
        print("Wiwat!")
    elif (num%7 == 0):
        print("Hurra!")
    elif (num%11 == 0):
        print("Super!")
    else:
        print(num)
