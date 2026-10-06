# 120902
# 문자열 계산하기

# 연산자가 2개 이상 포함되어 있을 수 있음.

# minus는 음수를 더하는 거로 변형해서, 양/음수의 합을 구하는 방법도 있음.

from collections import deque

def cal(a, op, b):
    if (op == '+'):
        return str(int(a) + int(b))
    elif (op == '-'):
        return str(int(a) - int(b))
    
def solution(my_string):
    ss = deque(my_string.split())
    
    while (len(ss) > 1):
        a, op, b = ss.popleft(), ss.popleft(), ss.popleft()
        ss.appendleft(cal(a, op, b))
        
    return int(ss[0])
