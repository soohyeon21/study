# 세 개의 구분자

def solution(myStr):
    answer = myStr.replace('a', ' ').replace('b', ' ').replace('c', ' ').split()
    
    if (len(answer) == 0):
        return ['EMPTY']
    else:
        return answer
