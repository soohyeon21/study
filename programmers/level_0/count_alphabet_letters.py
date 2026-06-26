# 문자 개수 세기

def solution(my_string):
    answer = [my_string.count(chr(i1)) for i1 in range(65, 91)] + [my_string.count(chr(i2)) for i2 in range(97, 123)]
    
    return answer
