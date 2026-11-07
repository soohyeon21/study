# 181916
# 주사위 게임 3

def solution(a, b, c, d):
    nlist = [a, b, c, d]
    diff = list(set(nlist))
    answer = 0
    
    if (len(diff) == 4):
        answer = min(a, b, c, d)
    elif (len(diff) == 3):
        for i in range(3):
            if (nlist.count(diff[i]) != 2):
                if (answer != 0):
                    answer *= diff[i]
                else:
                    answer += diff[i]
    elif (len(diff) == 2):
        if (nlist.count(diff[0]) == 2):
            answer = (diff[0]+diff[1]) * abs(diff[0]-diff[1])
        else:
            if (nlist.count(diff[0]) == 1):
                answer = (10*diff[1]+diff[0])**2
            else:
                answer = (10*diff[0]+diff[1])**2
    elif (len(diff) == 1):
        answer = 1111 * diff[0]
    
    return answer
