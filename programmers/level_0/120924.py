# 120924
# 다음에 올 숫자

# 미리 d, r을 구하고 등비/등차 판단했더니 오답.
# 등차인지 먼저 확인하고, 아니면 등비 확인해야 함.
# +) 공비는 '0이 아닌 정수'이지만, common의 값 자체는 (-1000, 2000).

def solution(common):
    d1, d2 = common[1]-common[0], common[2]-common[1]
    if (d1 == d2):
        return common[-1]+d1
    
    r = common[1]//common[0]
    return common[-1]*r
