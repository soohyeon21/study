# 간단한 식 계산하기

def solution(binomial):
    a, op, b = binomial.split()
    
    if (op == '+'):
        return int(a) + int(b)
    elif (op == '-'):
        return int(a) - int(b)
    elif (op == '*'):
        return int(a) * int(b)
