# 120893
# 대문자와 소문자

def solution(my_string):
    answer = ''
    for letter in my_string:
        if (ord(letter) < 91):
            answer += chr(ord(letter) + 32)
        else:
            answer += chr(ord(letter) - 32)
            
    return answer
