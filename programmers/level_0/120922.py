# 120922
# 종이 자르기

# 결국 M*N-1

def solution(M, N):
    answer = max(M, N)-1 + (min(M, N)-1)*max(M, N)
    return answer
