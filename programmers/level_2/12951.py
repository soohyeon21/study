# 12951
# JadenCase 문자열 만들기

# '공백문자가 연속해서 나올 수 있습니다.'

# 공백 2개 이상이 연속한 경우 문제 해결
# sol1) word == '' 인지 확인
# sol2) word[0]말고 word[0:1]로 대체

# 'a  b'.split(' ') # ['a', '', ''b]

###
### sol1) word == '' 인지 확인
###
# def solution(s):
#     answer = ''
#
#     word = ''
#     for i in range(len(s)):
#         if (s[i] == ' '):
#             if (word == ''):
#                 answer += ' '
#             else:
#                 answer += word[0].upper() + word[1:].lower()
#                 answer += ' '
#                 word = ''
#         else:
#             word += s[i]
#
#     if (word != ''):
#         answer += word[0].upper() + word[1:].lower()
#
#     return answer



###
### sol2) word[0]말고 word[0:1]로 대체
###
def solution(s):
    answer = ''
    
    word = ''
    for i in range(len(s)):
        if (s[i] == ' '):
            answer += word[0:1].upper() + word[1:].lower()
            answer += ' '
            word = ''
        else:
            word += s[i]
            
    if (word != ''):
        answer += word[0].upper() + word[1:].lower()
    
    return answer
