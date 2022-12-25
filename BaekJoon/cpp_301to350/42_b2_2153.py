# 2153

import sys
import math

def isPrime(num):
    isprime = True
    if (num == 1):
        return isprime
    
    for i in range(2, int(math.sqrt(num)) + 1):
        if (num % i == 0):
            isprime = False
    return isprime

word = sys.stdin.readline().rstrip()
wsum = 0
for letter in word:
    if (letter.islower()):
        wsum += ord(letter) - 96
    else:
        wsum += ord(letter) - 38
        
if (isPrime(wsum)):
    print("It is a prime word.")
else:
    print("It is not a prime word.")
