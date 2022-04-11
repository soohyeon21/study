# 10768

# 후루룩 하고 후루룩 제출했더니 후루룩 틀려버렸다ㅋㅋㅋ

import sys

m = int(sys.stdin.readline())
d = int(sys.stdin.readline())

if (m < 2):
    print("Before")
elif ((m == 2) and (d < 18)):
    print("Before")
elif ((m == 2) and (d == 18)):
    print("Special")
else:
    print("After")
