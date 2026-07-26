# 특정한 문자를 대문자로 바꾸기

# replace(alp, alp.upper()) 도 가능.

def solution(my_string, alp):
    return my_string.replace(alp, chr(ord(alp)-32))
