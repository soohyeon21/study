# 120896
# 한 번만 등장한 문자

def solution(s):
    answer = sorted([letter for letter in s if s.count(letter)==1])
    return ''.join(answer)
