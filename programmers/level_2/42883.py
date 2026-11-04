# 42883
# 큰 수 만들기

# monotonic stack(단조 스택)의 대표적 유형.

def solution(number, k):
    stack = []
    
    for num in number:
        while (stack and (stack[-1] < num) and (k > 0)):
            stack.pop()
            k -= 1
        stack.append(num)
    
    if (k > 0):
        stack = stack[:-1]
    
    return ''.join(stack)
