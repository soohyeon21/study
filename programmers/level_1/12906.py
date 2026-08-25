# 12906
# 같은 숫자는 싫어

# or (stack[-1:] != arr[i])로 표현하는 방법 → stack=[]로 시작 가능
# or len(stack)==0을 확인하는 방법

def solution(arr):
    stack = [arr[0]]
    for i in range(1, len(arr)):
        if (stack[-1] != arr[i]):
            stack.append(arr[i])
    return stack
