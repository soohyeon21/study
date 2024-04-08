# 26489

# 왜 try-except/try-except EOFError에서 input()을 쓰면 맞고,
# sys.stdin.readline() or sys.stdin.readline().rstrip()을 쓰면 틀릴까?

#
# sol1) try-except 없이 sys.stdin.readline().rstrip()
#
import sys

##cnt = 0
##while (1):
##    data = sys.stdin.readline().rstrip()
##    if (data == ""):
##        break
##    cnt += 1
##
##print(cnt)



#
# sol2) input(), except
#
##cnt = 0
##while (1):
##    try:
##        data = input()
##        cnt += 1
##    except:
##        break
##
##print(cnt)



#
# sol3) input(), except EOFError
#
cnt = 0
while (1):
    try:
        data = input()
        cnt += 1
    except EOFError:
        break

print(cnt)
