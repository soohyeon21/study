# 28702

# "연속으로 출력된 세 개의 문자열 다음에 올 문자열을 출력하세요. 여러 문자열이 올 수 있는 경우, 아무거나 하나 출력하세요."
# 여러 문자열이 올 수 있는 경우가 존재하나?

# str.isnumeric()과 str.isdigit()의 차이?
# 거의 비슷. 일부 특수 경우에서만 조금 다른듯.
# isdigit()은 문자열이 '숫자'로만 이루어져 있어야 한다.
# "½".isdigit() # False
# "½".isnumeric() # True

import sys

ascen = [sys.stdin.readline().rstrip() for _ in range(3)]
number_idx = -1
for a in ascen:
    if (a.isdigit()):
        number_idx = ascen.index(a)

next_num = 3-number_idx + int(ascen[number_idx])

if ((next_num%3 == 0) and (next_num%5 == 0)):
    print("FizzBuzz")
elif ((next_num%3 == 0) and (next_num%5 != 0)):
    print("Fizz")
elif ((next_num%3 != 0) and (next_num%5 == 0)):
    print("Buzz")
else:
    print(next_num)
