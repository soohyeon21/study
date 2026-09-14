# 181836
# 그림 확대

# replace(before, before*k) 활용 가능.

def solution(picture, k):
    answer = []
    
    for i in range(len(picture)):
        newline = ''
        for letter in picture[i]:
            newline += letter*k
        for j in range(k):
            answer.append(newline)
        
    return answer
