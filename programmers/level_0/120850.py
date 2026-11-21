# 120850
# 문자열 정렬하기 (1)

def solution(my_string):
    answer = []
    for letter in my_string:
        if (letter.isdigit()):
            answer.append(int(letter))
    
    return sorted(answer)
