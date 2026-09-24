# 120921
# 문자열 밀기

def solution(A, B):
    mul_A = A*2
    if (B not in mul_A):
        return -1
    
    for i in range(len(A)):
        if (mul_A[len(A)-i:len(A)*2-i] == B):
            return i
