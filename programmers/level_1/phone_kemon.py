# 폰켓몬

# dictionary 대신 set을 사용해도 됨.

def solution(nums):
    pmon = {}
    for num in nums:
        pmon[num] = pmon.setdefault(num, 0)
        pmon[num] += 1
        
    return min(len(pmon), len(nums)//2)
