# 길이에 따른 연산

# alist = [1, 2, 3, 4]

# from functool import reduce
# rval = reduce(lambda x, y: x*y, alist) # rval = 24

# from math import prod
# pval = prod(alist) # pval = 24

def solution(num_list):
    answer = 0
    if (len(num_list) > 10):
        answer = sum(num_list)
    else:
        answer = 1
        for i in range(len(num_list)):
            answer *= num_list[i]
    
    return answer
