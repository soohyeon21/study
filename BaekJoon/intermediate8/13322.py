# 13322

#
# sol1) 맞는 풀이
#
import sys

s = sys.stdin.readline().rstrip()
for i in range(len(s)):
    print(i)



#
# sol2) 메모리 초과
#
##import sys
##
##s = sys.stdin.readline().rstrip()
##
##pref = {s[:i]:len(s)-i for i in reversed(range(1, len(s)+1))}
##for pre in pref.keys():
##    print(pref[pre]
