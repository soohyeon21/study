# 120907
# OX퀴즈

def cal(x, op, y):
    if (op == '+'):
        return int(x) + int(y)
    elif (op == '-'):
        return int(x) - int(y)
    
def solution(quiz):
    answer = []
    for equ in quiz:
        x, op, y, eop, z = equ.split()
        if (int(z) == cal(x, op, y)):
            answer.append("O")
        else:
            answer.append("X")
    return answer
