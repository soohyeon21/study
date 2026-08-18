# 42839
# 소수 찾기

# from itertools import permutations, combinations
# alist = [1, 2, 3]
# list(permutations(alist, 2)) # [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
# list(combinations(alist, 2)) # [(1, 2), (1, 3), (2, 3)]

from collections import Counter

def solution(numbers):
    ## 소수인지 확인
    max_n = 10000000
    prime = [1 for _ in range(max_n+1)]
    prime[0], prime[1] = 0, 0
    for i in range(2, int(max_n**0.5)+1):
        for j in range(2, max_n//i+1):
            prime[i*j] = 0
    
    numbers_cnt = Counter(list(str(numbers)))
    
    ## 주어진 수 조합으로 만들어낼 수 있는 최대 수 찾기
    poss_max_num = int(''.join(sorted(list(numbers), reverse=True)))
    
    ## (0 ~ poss_max_num) 범위의 모든 수에 대해서
    ## 소수인지 확인하고
    ## 가능한 조합인지도 확인하기
    cnt = 0
    for num in range(poss_max_num+1): # 모든 수 확인
        if (prime[num]): # 소수인 경우만 확인
            pnum_cnt = Counter(list(str(num)))

            state = True # 가능한 숫자인지 확인
            for k, v in pnum_cnt.items():
                if ((k not in numbers_cnt) or (pnum_cnt[k] > numbers_cnt[k])):
                    state = False

            if (state):
                cnt += 1
    
    return cnt
