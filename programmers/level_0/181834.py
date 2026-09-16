# 181834
# l로 만들기

# A = 65
# Z = 90
# a = 97
# z = 122

def solution(myString):
    answer = ''
    for letter in myString:
        if (ord(letter) < 108):
            answer += 'l'
        else:
            answer += letter
    return answer
