# 문자열 잘라서 정렬하기

def solution(myString):
    slist = sorted(myString.split('x'))
    answer = []
    for each in slist:
        if (each != ''):
            answer.append(each)
    return answer
