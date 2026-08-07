# 문자열 바꿔서 찾기

def solution(myString, pat):
    altered = ""
    for letter in myString:
        if (letter == 'A'):
            altered += 'B'
        elif (letter == 'B'):
            altered += 'A'
        else:
            altered += letter
    
    if (pat in altered):
        return 1
    else:
        return 0
