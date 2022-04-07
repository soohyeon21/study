# 5656

# 아오 아무래도 그 수많은 시도가 틀렸던 이유는 피연산자를 int로 변환해주지 않아서인듯 하다...ㅎ
# 맞다. 그렇게 되면 내 첫 풀이도 맞는 풀이가 된다. 아오.

# 뭐가 int고 뭐가 str인지 명확히 구분하고 시작하자!!

#
# right
#
import sys

case = 1
operator = [">", ">=", "<", "<=", "==", "!="]
sta = True

while (True):
    eq = sys.stdin.readline().rstrip().split(" ")
    eq[0] = int(eq[0]) # 단순히 요 두 줄을 추가했더니
    eq[2] = int(eq[2]) # 맞는 풀이가 되어버렸다ㅎ
    if (eq[1] == "E"):
        break
    
    op = operator.index(eq[1])
    if (op == 0):
        sta = (eq[0] > eq[2])
    elif (op == 1):
        sta = (eq[0] >= eq[2])
    elif (op == 2):
        sta = (eq[0] < eq[2])
    elif (op == 3):
        sta = (eq[0] <= eq[2])
    elif (op == 4):
        sta = (eq[0] == eq[2])
    elif (op == 5):
        sta = (eq[0] != eq[2])

    status = str(sta).lower()

    print("Case {}: {}" .format(case, status))
    case += 1

#
# right
#
##import sys
##
##case = 1
##sta = True
##
##while (True):
##    eq = sys.stdin.readline().rstrip().split()
##    eq[0] = int(eq[0])
##    eq[2] = int(eq[2])
##    if (eq[1] == "E"):
##        break
##    elif (eq[1] == ">"):
##        sta = (eq[0] > eq[2])
##    elif (eq[1] == ">="):
##        sta = (eq[0] >= eq[2])
##    elif (eq[1] == "<"):
##        sta = (eq[0] < eq[2])
##    elif (eq[1] == "<="):
##        sta = (eq[0] <= eq[2])
##    elif (eq[1] == "=="):
##        sta = (eq[0] == eq[2])
##    elif (eq[1] == "!="):
##        sta = (eq[0] != eq[2])
##
##    status = str(sta).lower()
##
##    print("Case {}: {}" .format(case, status))
##    case += 1
