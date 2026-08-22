# 181855
# 문자열 묶기

from collections import defaultdict

def solution(strArr):
    ldict = defaultdict(int)
    for word in strArr:
        ldict[len(word)] += 1
    
    return max(ldict.values())
