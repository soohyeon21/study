# 10174

#
# 틀린 풀이
# rstrip()을 하면서 끝의 "\n"이 아닌 단순 공백도 없애버렸기 때문인듯 하다.
# rstrip() 대신 replace("\n", "") 해주면 해결된다.
#
##import sys
##
##n = int(sys.stdin.readline())
##for _ in range(n):
##    linea = sys.stdin.readline().rstrip().lower()
##    if (linea == linea[::-1]):
##        print("Yes")
##    else:
##        print("No")

#
# sol1
#
##n = int(input())
##for _ in range(n):
##    line = input().lower()
##    if (line == line[::-1]):
##        print("Yes")
##    else:
##        print("No")

#
# sol2
#
import sys

n = int(sys.stdin.readline())
for _ in range(n):
    linea = sys.stdin.readline().replace("\n", "").lower()
    if (linea == linea[::-1]):
        print("Yes")
    else:
        print("No")
