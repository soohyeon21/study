# 4690

#
# sol1) PyPy3 정답, Python3 시간초과
#
##import sys
##
##ssang = []
##for a in range(2, 101):
##    for b in range(2, 101):
##        for c in range(b+1, 101):
##            for d in range(c+1, 101):
##                if (a**3 == b**3 + c**3 + d**3):
##                    ssang.append((a, b, c, d))
##
##for ss in ssang:
##    print(f"Cube = {ss[0]}, Triple = ({ss[1]},{ss[2]},{ss[3]})")



#
# sol2) 경우의 수 줄이기. PyPy3d와 Python3 모두 정답
#
import sys

ssang = []
for a in range(2, 101):
    for b in range(2, 101):
        for c in range(b+1, 101):
            for d in range(c+1, 101):
                if (a**3 == b**3 + c**3 + d**3):
                    ssang.append((a, b, c, d))
                if (a**3 < b**3 + c**3 + d**3):
                    break

for ss in ssang:
    print(f"Cube = {ss[0]}, Triple = ({ss[1]},{ss[2]},{ss[3]})")
