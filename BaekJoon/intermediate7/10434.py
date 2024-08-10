# 10434

import sys

def isPrime(num):
    if (num == 1):
        return False
    if (num == 2):
        return True
    for i in range(2, int(num**0.5)+1):
        if (num%i == 0):
            return False
    return True


p = int(sys.stdin.readline())
for _ in range(p):
    tnum, m = map(int, sys.stdin.readline().split())

    state = "NO"
    if (isPrime(m)):
        already = []
        sqnum = m
        while (1):
            sqnum = sum(int(digit)**2 for digit in str(sqnum))
            if (sqnum == 1):
                state = "YES"
                break
            if (sqnum not in already):
                already.append(sqnum)
            else:
                break

    print(f"{tnum} {m} {state}")
