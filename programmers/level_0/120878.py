# 120878
# 유한소수 판별하기

def gcf(a, b):
    while (b != 0):
        num = a%b
        a = b
        b = num
    return a

def solution(a, b):
    gcf_ab = gcf(a, b)
    a //= gcf_ab # 불필요
    b //= gcf_ab
    
    for i in range(10):
        if (b%2 == 0):
            b //= 2
        if (b%5 == 0):
            b //= 5
    
    answer = 2
    if (b == 1):
        answer = 1
        
    return answer
