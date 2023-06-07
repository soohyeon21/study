# 16968

# 한 번 사용한 숫자/문자를 다시 사용할 수 있다. 연속되지만 않는다면!

# 모든 경우를 따져 푸는 것보다, 직전 자리와 연속인지 여부만 판단해서 간단하게 푸는 방법이 더 나은듯.

import sys

plate = sys.stdin.readline().rstrip()
cnt = 0
rest = 0

if ("cccc" in plate):
    cnt = 26*25*25*25
elif ("dddd" in plate):
    cnt = 10*9*9*9
elif ("ccc" in plate):
    cnt = 26*25*25
    rest = 10**plate.count("d")
elif ("ddd" in plate):
    cnt = 10*9*9
    rest = 26**plate.count("c")
elif (("cc" in plate) and ("dd" in plate)):
    cnt = 26*25*10*9
elif ("cc" in plate):
    cnt = 26*25
    rest = 10**plate.count("d") * 26**(plate.count("c")-2)
elif ("dd" in plate):
    cnt = 10*9
    rest = 26**plate.count("c") * 10**(plate.count("d")-2)
else:
    cnt = 26**plate.count("c") * 10**plate.count("d")

if (rest):
    cnt *= rest

print(cnt)
