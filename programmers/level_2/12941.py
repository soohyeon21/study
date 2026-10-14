# 12941
# 최솟값 만들기

# 재배열 부등식(Rearrangement Inequality) # 아래 풀이에서는 항상 min값이 보장된다!

def solution(A,B):
    answer = 0
    A = sorted(A)
    B = sorted(B, reverse=True)
    
    for i in range(len(A)):
        answer += A[i] * B[i]
    
    return answer
