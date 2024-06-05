# 1972

import sys

while (1):
    string = sys.stdin.readline().rstrip()
    if (string == "*"):
        break

    state = ""
    for i in range(1, len(string)-1):
        pair = [string[k]+string[k+i] for k in range(len(string)-i)]
        if (len(set(pair)) != len(pair)):
            state = "NOT "
            break

    print(f"{string} is {state}surprising.")
