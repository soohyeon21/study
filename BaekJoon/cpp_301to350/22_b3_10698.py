# 10698

import sys

n = int(sys.stdin.readline())
for i in range(1, n+1):
    answer = ""
    equation = sys.stdin.readline().split()
    if ((equation[1] == "+") and (int(equation[4]) == int(equation[0]) + int(equation[2]))):
        answer = "YES"
    elif ((equation[1] == "-") and (int(equation[4]) == int(equation[0]) - int(equation[2]))):
        answer = "YES"
    else:
        answer = "NO"
    print(f"Case {i}: {answer}")
