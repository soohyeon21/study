# 의상

# from collections import Counter
# a = Counter(a1 for a1, a2 in [(1, 11), (2, 22), (1, 44), (3, 33)])
# >>> a = {1:2, 2:1, 3:1}

# from collections import defaultdict
# wardrobe = defaultdict(list)

def solution(clothes):
    wardrobe = {}
    for cloth in clothes:
        wardrobe[cloth[1]] = wardrobe.setdefault(cloth[1], [])
        wardrobe[cloth[1]].append(cloth[0])
    
    cases = 1
    for k, v in wardrobe.items():
        cases *= len(v)+1
    ## or reduce 사용해서 경우의 수 구하기
    # from functool import reduce
    # cases = reduce(lambda x, y:x*(y+1), wardrobe.values(), 1)
    
    return cases-1
