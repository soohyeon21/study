# 120853
# 컨트롤 제트

def solution(s):
    s = s.split()
    for i in range(1, len(s)):
        if (s[i] == 'Z'):
            s[i-1] = '0'
    
    answer = 0
    for each in s:
        if ((each.isdigit()) or ('-' in each)):
            answer += int(each)
    
    return answer
