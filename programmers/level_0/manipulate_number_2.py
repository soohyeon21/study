# 수 조작하기 2

def solution(numLog):
    match = {1:'w', -1:'s', 10:'d', -10:'a'}
    
    stringi = ''
    for i in range(1, len(numLog)):
        stringi += match[numLog[i]-numLog[i-1]]
        
    return stringi
