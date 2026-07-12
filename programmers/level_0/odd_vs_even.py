# 홀수 vs 짝수

def solution(num_list):
    odd, even = 0, 0
    for i in range(len(num_list)):
        if (i%2 == 0):
            odd += num_list[i]
        elif (i%2 == 1):
            even += num_list[i]
    
    return max(odd, even)
