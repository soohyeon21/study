# 17122

# 변수 이름 조심!

import sys
import math

t = int(sys.stdin.readline())

bstart = [1, 3, 5, 7]
for _ in range(t):
    alp, dig = sys.stdin.readline().split()
    a_status = ''
    d_status = ''

    plus = 0
    if (int(alp[1]) not in bstart):
        plus = 1
    a_status = ['black', 'white'][(ord(alp[0])-65+plus)%2]

    row = math.ceil(int(dig)/8)
    plus2 = 0
    if (row not in bstart):
        plus2 = 1
    d_status = ['white', 'black'][(int(dig)+plus2)%2]

    if (a_status == d_status):
        print("YES")
    else:
        print("NO")
