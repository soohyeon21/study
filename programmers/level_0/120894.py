# 120894
# 영어가 싫어요

# or .replace('one', '1') 이런식으로.

def solution(numbers):
    english = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    
    num = ''
    answer = ''
    for i in range(len(numbers)):
        num += numbers[i]
        if (num in english):
            answer += str(english[num])
            num = ''
    
    return int(answer)
