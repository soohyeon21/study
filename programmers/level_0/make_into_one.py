# 1로 만들기

def solution(num_list):
    cnt = 0
    for num in num_list:
        while (1):
            if (num == 1):
                break
            
            if (num % 2 == 0): # 굳이 홀짝 구분 안해도 됨.
                num //= 2
            elif (num % 2 == 1):
                num = (num-1)//2
            cnt += 1
    
    return cnt
