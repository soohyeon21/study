# 120871
# 저주의 숫자 3

def solution(n):
    threev = {}
    
    three = 0
    for gen in range(1, 101):
        three += 1
        while ((three%3 == 0) or ('3' in str(three))):
            three += 1
        threev[gen] = three
    
    return threev[n]
