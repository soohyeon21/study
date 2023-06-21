# 26594

# "어떤 알파벳도 두 번 이상 입력하지 않는다."
# 따라서 간단하게 sol2로 풀어도 된다.

#
#sol1
#
##import sys
##
##wrong = sys.stdin.readline().rstrip()
##first = wrong[0]
##cnt = 0
##for i in range(len(wrong)):
##    if (wrong[i] == first):
##        cnt += 1
##    else:
##        break
##
##print(cnt)

#
# sol2
#
import sys

wrong = sys.stdin.readline().rstrip()
print(wrong.count(wrong[0]))
