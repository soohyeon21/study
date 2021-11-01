# 2747

# 시간 내에.

import sys

n = int(sys.stdin.readline())

fibo = [0, 1]
for i in range(2, n+1):
    fibo.append(fibo[i-2] + fibo[i-1])

print(fibo[n])



##import sys
##
##def fibonacci(n):
##    if (n == 0):
##        return 0
##    elif (n == 1):
##        return 1
##    else:
##        return (fibonacci(n-1) + fibonacci(n-2))
##
##n = int(sys.stdin.readline())
##
##print(fibonacci(n))
