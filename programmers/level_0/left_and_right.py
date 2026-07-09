# 왼쪽 오른쪽

# 그냥 for문으로 찾으면서, 먼저 찾는 l or r 보고 판단하는 방법도 있음.
# l or r 중에서 하나만 존재해도 괜찮음.

def solution(str_list):
    l, r = 20, 20
    for i in range(len(str_list)):
        if ((str_list[i] == 'l') and (l == 20)):
            l = i
        if ((str_list[i] == 'r') and (r == 20)):
            r = i
    
    if ((l == 20) and (r == 20)):
        return []
    elif (l < r):
        return str_list[:l]
    elif (r < l):
        return str_list[r+1:]
