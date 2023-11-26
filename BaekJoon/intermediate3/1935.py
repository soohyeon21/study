# 1935

# isnumeric() vs isdigit()
# isdecimal()

#
# sol1) 그냥 처음 생각으로 푼 방법
# Python3&PyPy3 시간초과...
#
##import sys
##
##def postfix(equation):
##    op = ["+", "-", "*", "/"]
##    while (("*" in equation) or ("/" in equation)): # 괄호가 존재하면 사용할 수 없는 방법. + or -를 해야 * or /를 계산할 수 있는 경우도 있으므로.
##        for j in range(len(equation)-2):
##            if ((equation[j] not in op) and (equation[j+1] not in op) and (equation[j+2] == "*")):
##                equation = equation[:j] + [equation[j] * equation[j+1]] + equation[j+3:]
##                break
##            if ((equation[j] not in op) and (equation[j+1] not in op) and (equation[j+2] == "/")):
##                equation = equation[:j] + [equation[j] / equation[j+1]] + equation[j+3:]
##                break
##    while (("+" in equation) or ("-" in equation)):
##        for j in range(len(equation)-2):
##            if ((equation[j] not in op) and (equation[j+1] not in op) and (equation[j+2] == "+")):
##                equation = equation[:j] + [equation[j] + equation[j+1]] + equation[j+3:]
##                break
##            if ((equation[j] not in op) and (equation[j+1] not in op) and (equation[j+2] == "-")):
##                equation = equation[:j] + [equation[j] - equation[j+1]] + equation[j+3:]
##                break
##            
##    return equation[0]
##
##n = int(sys.stdin.readline())
##eq = sys.stdin.readline().rstrip()
##alpha = {chr(i):int(sys.stdin.readline()) for i in range(65, 65+n)}
##
### 알파벳에 숫자 대입하기
##trans = []
##for each in eq:
##    if (each.isalpha()):
##        trans.append(alpha[each])
##    else:
##        trans.append(each)
##
##print(f"{postfix(trans):.2f}")



#
# sol2) 후위표기식-stack 사용
# cal(b, a, op) 순으로 하면 stack에서 pop할때 a와 b의 순서를 신경쓰지 않아도 된다. 굿!
#
import sys

def cal(b, a, op):
    if (op == "+"):
        return a+b
    elif (op == "-"):
        return a-b
    elif (op == "*"):
        return a*b
    elif (op == "/"):
        return a/b

n = int(sys.stdin.readline())
eq = sys.stdin.readline().rstrip()
table = {chr(i):int(sys.stdin.readline()) for i in range(65, 65+n)}

rand = []
for term in eq:
    if (term.isalpha()):
        rand.append(table[term])
    else:
        rand.append(cal(rand.pop(), rand.pop(), term))

print(f"{rand[0]:.2f}")
