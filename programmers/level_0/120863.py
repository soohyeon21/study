# 120863
# 다항식 더하기

def solution(polynomial):
    polynomial = polynomial.split(' + ')
    x1, x0 = 0, 0
    for each in polynomial:
        if (each[-1] == 'x'):
            if (len(each) == 1):
                x1 += 1
            else:
                x1 += int(each[:-1])
        else:
            x0 += int(each)
    
    answer = ""
    if (x1 == 0):
        answer = f"{x0}"
    elif (x1 == 1):
        if (x0 == 0):
            answer = "x"
        else:
            answer = f"x + {x0}"
    else: # (x1 > 1)
        if (x0 == 0)   :
            answer = f"{x1}x"
        else:
            answer = f"{x1}x + {x0}"
    
    return answer
