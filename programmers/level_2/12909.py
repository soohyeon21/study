# 12909
# 올바른 괄호

def solution(s):
    state = True
    
    stack = []
    for one in s:
        if (one == '('):
            stack.append('(')
        elif (one == ')'):
            if (not stack):
                state = False
                break # return False
            if (stack[-1] != '('):
                state = False
                break
            if (stack[-1] == '('):
                stack.pop()
    
    if (stack):
        state = False
    
    return state
