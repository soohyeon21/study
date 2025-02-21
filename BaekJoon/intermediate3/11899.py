# 11899

#
# sol1) variable 사용하기
#
##import sys
##
##s = sys.stdin.readline().rstrip()
##
##c_bra = 0
##o_bra = 0
##for i in range(len(s)):
##    if (s[i] == '('):
##        o_bra += 1
##    elif (s[i] == ')'):
##        if (o_bra > 0):
##            o_bra -= 1
##        else:
##            c_bra += 1
##
##print(c_bra + o_bra)



#
# sol2) stack에 넣고 빼기
#
import sys

s = sys.stdin.readline().rstrip()

stack = []
for one in s:
    if (one == "("):
        stack.append(one)
    elif (stack and (stack[-1] == "(")):
        stack.pop()
    else:
        stack.append(one)

print(len(stack))
