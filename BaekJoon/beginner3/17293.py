# 17293

# while 대신 for 쓰는 방법
# 마지막 출력만 loop에서 제외해서 별도로 다루는 방법

import sys

def choose(n):
    plural = ""
    if (n >= 2):
        plural = f"{n} bottles"
    elif (n == 1):
        plural = "1 bottle"
    elif (n == 0):
        plural = "No more bottles"
    elif (n == -1):
        plural = choose(first)

    return plural

n = int(sys.stdin.readline())
first = n

while (n >= 0):
    print(f"{choose(n)} of beer on the wall, {choose(n).lower()} of beer.")
    print("Take one down and pass it around, " if n>0 else "Go to the store and buy some more, ", end="")
    print(f"{choose(n-1).lower()} of beer on the wall.\n")

    n -= 1
