# 120869
# 외계어 사전

# 단, ex) abc-abbc 인 경우에 대한 문제 있음.

def solution(spell, dic):
    answer = 2
    for each in dic:
        if (set(each) == set(spell)):
            answer = 1
    return answer
