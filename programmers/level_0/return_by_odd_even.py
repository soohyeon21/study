# 홀짝에 따라 다른 값 반환하기

# sum(1 ~ n) # n(n+1) / 2
# sum(1**2 ~ n**2) # n(n+1)(2n+1) / 6
# sum(1**3 ~ n**3) # {n(n+1) / 2}**2

def solution(n):
    result = 0
    if (n % 2 == 1):
        result = (n//2+1)**2
    elif (n % 2 == 0):
        for i in range(1, n//2+1):
            result += (i*2)**2
    
    return result
