# 120911
# 문자열 정렬하기 (2)

def solution(my_string):
    answer = []
    for i in range(len(my_string)):
        answer.append(ord(my_string[i].lower()))
    answer.sort()
    
    anss = []
    for k in range(len(answer)):
        anss.append(chr(answer[k]))
    jans = ''.join(anss)
    return jans
