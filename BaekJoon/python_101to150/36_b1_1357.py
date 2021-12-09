# 1357

# 자연수 = 양의 정수

# a[::-1] # "abc" -> "cba"로 바꿔줌

import sys

def Rev(numi):
    num_str = str(numi)
    numo = ""
    for number in num_str:
        numo = number + numo
    num_int = int(numo)
    return num_int

x, y = map(int, sys.stdin.readline().split())
print(Rev(Rev(x) + Rev(y)))
