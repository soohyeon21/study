# 12871

# 길이가 더 작은 문자열을 더 긴 문자열에서 ''으로 replace하는 경우 => 'aa'&'aaa'일때 문제 발생

# 사실 그냥 단순히 t에는 len(s)만큼을, s에는 len(t)만큼을 곱해줬어도 됐다. 굳이 LCM까지 찾지 않아도 충분했다.

import sys

def gcf(a, b):
    while (b != 0):
        num = a%b
        a = b
        b = num
    return a

def lcm(a, b):
    return a*b//gcf(a, b)


s = sys.stdin.readline().rstrip()
t = sys.stdin.readline().rstrip()

common = lcm(len(s), len(t))
t *= common//len(t)
s *= common//len(s)

if (t == s):
    print(1)
else:
    print(0)
