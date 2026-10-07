# 49993
# 스킬트리

def solution(skill, skill_trees):
    cnt = 0
    for i in range(len(skill_trees)):
        tmp = []
        for k in range(len(skill)):
            if (skill[k] in skill_trees[i]):
                tmp.append(skill_trees[i].find(skill[k]))
            else:
                tmp.append(26)
        
        inOrder = True
        for p in range(len(tmp)-1):
            if (tmp[p] > tmp[p+1]):
                inOrder = False
        # print(skill_trees[i], tmp, inOrder)
        
        if (inOrder):
            cnt += 1
    
    return cnt
