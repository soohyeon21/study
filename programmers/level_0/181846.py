# 181846
# 두 수의 합

# ## sol1) 직접 자리별 수의 합 구해서 문자열로 합치기 방법

# def solution(a, b):
#     result = [0] * (max(len(a), len(b))+1)
    
#     for i in range(len(a)):
#         result[i] += int(a[::-1][i])
#     #print(result)
#     for j in range(len(b)):
#         result[j] += int(b[::-1][j])
#     #print(result)
    
#     for k in range(len(result)-1):
#         if (result[k] > 9):
#             result[k+1] += result[k]//10
#             result[k] %= 10
#     #print(result)
    
#     answer = ''.join(map(str, result))[::-1].lstrip('0')
#     if (answer == ''):
#         answer = '0'
        
#     return answer



## sol2) python 3.11 이상: DoS 방지 위해 str-int 4,300자리 숫자로 제한함.
import sys

sys.set_int_max_str_digits(100000)

def solution(a, b):
    return str(int(a) + int(b))
