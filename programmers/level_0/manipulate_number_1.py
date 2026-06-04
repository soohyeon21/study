# 수 조작하기 1

def solution(n, control):
    change = {'w':1, 's':-1, 'd':10, 'a':-10}
    
    answer = n
    for letter in control:
        answer += change[letter]
    
    return answer
