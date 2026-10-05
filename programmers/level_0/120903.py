# 120903
# 배열의 유사도

# set() & # 교집합
# set() | # 합집합
# set() - # 차집합

# def solution(s1, s2):
#     return len(s1) - len(set(s1)-set(s2))

def solution(s1, s2):
    answer = 0
    for ele in s1:
        if (ele in s2):
            answer += 1
    return answer
