# 배열 만들기 5

def solution(intStrs, k, s, l):
    answer = []
    for element in intStrs:
        cut = int(element[s:l+s])
        if (cut > k):
            answer.append(cut)
    return answer
