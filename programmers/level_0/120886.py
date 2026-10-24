# 120886
# A로 B 만들기

# sorted('abc') # ['a', 'b', 'c']

from collections import defaultdict

def solution(before, after):
    bdict = defaultdict(int)
    adict = defaultdict(int)
    
    for i in range(len(before)):
        bdict[before[i]] += 1
        adict[after[i]] += 1
    
    if (bdict == adict):
        return 1
    return 0
