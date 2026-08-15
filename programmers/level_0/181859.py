# 181859
# 배열 만들기 6

def solution(arr):
    stk = []
    i = 0
    while (1):
        if (i >= len(arr)):
            break

        if (len(stk) == 0):
            stk.append(arr[i])
        elif (stk[-1] == arr[i]):
            stk.pop()
        else:
            stk.append(arr[i])
        i += 1
    
    if (len(stk) == 0):
        return [-1]
    else:
        return stk
