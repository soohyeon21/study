# 16503

#
# sol1) deque&stack으로 풀어봤으나, 굳이 복잡하게 푼 듯하다.
#
##import sys
##from collections import deque
##
##def cal(operator, oprand1, oprand2):
##    if (operator == "+"):
##        return oprand1 + oprand2
##    elif (operator == "-"):
##        return oprand1 - oprand2
##    elif (operator == "*"):
##        return oprand1 * oprand2
##    elif (operator == "/"):
##        if (oprand1*oprand2 < 0):
##            return abs(oprand1)//abs(oprand2) * -1
##        else:
##            return oprand1 // oprand2
##    
##equ = sys.stdin.readline().split()
##result = []
##
##first_opr = deque([equ[1], equ[3]])
##first_opd = deque(map(int, [equ[0], equ[2], equ[4]]))
##first_opd.appendleft(cal(first_opr.popleft(), first_opd.popleft(), first_opd.popleft()))
##result.append(cal(first_opr.pop(), first_opd.popleft(), first_opd.popleft()))
##
##op = [equ[1], equ[3]]
##rand = list(map(int, [equ[0], equ[2], equ[4]]))
##end = rand.pop()
##rand.append(cal(op.pop(), rand.pop(), end))
##end = rand.pop()
##result.append(cal(op.pop(), rand.pop(), end))
##
##print(f"{min(result)}\n{max(result)}")



#
# sol2) 간단하게. 마치 괄호를 내가 만들어준 느낌이다.
# 개인적으로 cal(a, op, b) 순서로 지정한 부분이 마음에 든다.
#
import sys

def cal(a, op, b):
    a, b = int(a), int(b)
    if (op == "+"):
        return a + b
    elif (op == "-"):
        return a - b
    elif (op == "*"):
        return a * b
    elif (op == "/"):
        return a // b if (a*b>0) else abs(a)//abs(b)*-1

k1, o1, k2, o2, k3 = sys.stdin.readline().split()

result = [cal(cal(k1, o1, k2), o2, k3), cal(k1, o1, cal(k2, o2, k3))]
print(f"{min(result)}\n{max(result)}")
