# 181921
# 배열 만들기 2

def solution(l, r):
    answer = []
    for num in range(l, r+1):
        if (set(list(str(num))) in [{'0', '5'}, {'0'}, {'5'}]):
            answer.append(num)
    
    answer.sort()
    
    if (not answer):
        answer.append(-1)
    
    return answer
