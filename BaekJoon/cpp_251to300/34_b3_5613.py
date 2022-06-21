# 5613

# 숫자, 숫자+연산자 2개씩 묶어서 처리하는 방법도 있다.

import sys

val = 0
op = "+"
four = [42, 43, 45, 47]

while (1):
    inp = sys.stdin.readline().rstrip()
    if (inp == "="):
        break

    if (ord(inp[0]) not in four):
        if (op == "+"):
            val += int(inp)
        elif (op == "-"):
            val -= int(inp)
        elif (op == "*"):
            val *= int(inp)
        elif (op == "/"):
            val //= int(inp)
    else:
        op = inp
print(val)
