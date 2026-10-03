# 120904
# 숫자 찾기

def solution(num, k):
    place = str(num).find(str(k))
    if (place != -1):
        return place + 1
    return place
