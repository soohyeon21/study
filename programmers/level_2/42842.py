# 42842
# 카펫

def solution(brown, yellow):
    lattice = brown + yellow
    for h in range(1, int(lattice**0.5)+1):
        if (lattice%h != 0):
            continue
        w = lattice//h
        if ((brown == (h-1 + w-1)*2) and (yellow == (w-2)*(h-2))):
            return [w, h]
