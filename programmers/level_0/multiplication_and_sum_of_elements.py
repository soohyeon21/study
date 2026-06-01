# 원소들의 곱과 합

def solution(num_list):
    mul = 1
    ssum = sum(num_list)**2
    for i in range(len(num_list)):
        mul *= num_list[i]
        
    if (mul < ssum):
        return 1
    elif (mul > ssum): # (mul == sum)인 경우는 없나? 고려 안하나??
        return 0
