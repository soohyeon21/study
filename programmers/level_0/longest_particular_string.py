# 특정 문자열로 끝나는 가장 긴 부분 문자열 찾기

# rfind(), rindex()

def solution(myString, pat):
    end_idx = len(myString)-1 - myString[::-1].index(pat[::-1])
    answer = myString[:end_idx+1]
    return answer
