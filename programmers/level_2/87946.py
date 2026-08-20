# 87946
# 피로도

# DFS로도 가능한 듯?

from itertools import permutations

def solution(k, dungeons):
    explore = list(permutations(dungeons))
    
    max_cnt = 0
    for i in range(len(explore)):
        cnt = 0
        hp = k
        for p in range(len(dungeons)):
            if (hp >= explore[i][p][0]):
                cnt += 1
                hp -= explore[i][p][1]
            else:
                break
        max_cnt = max(max_cnt, cnt)
    
    return max_cnt
