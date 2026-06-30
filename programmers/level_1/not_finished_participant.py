# 완주하지 못한 선수

def solution(participant, completion):
    pdict = {}
    for one in participant:
        pdict[one] = pdict.setdefault(one, 0)
        pdict[one] += 1
    
    for comp in completion:
        pdict[comp] -= 1

    for k, v in pdict.items():
        if (v > 0):
            return k
