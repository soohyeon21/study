# 등차수열의 특정한 항만 더하기

def solution(a, d, included):
    acnt = 0
    dcnt = 0
    for i in range(len(included)):
        if (included[i]):
            acnt += 1
            dcnt += i
    
    return acnt*a + dcnt*d
