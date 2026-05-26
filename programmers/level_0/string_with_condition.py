# 조건 문자열

def solution(ineq, eq, n, m):
    state = True
    if (ineq + eq == '>='):
        if not (n >= m):
            state = False
    elif (ineq + eq == '<='):
        if not (n <= m):
            state = False
    elif (ineq + eq == '>!'):
        if not (n > m):
            state = False
    elif (ineq + eq == '<!'):
        if not (n < m):
            state = False
    
    return int(state)
