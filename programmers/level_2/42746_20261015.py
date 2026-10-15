# 42746
# 가장 큰 수

# ##+) 여전히 이해 안가는...
# # def compare_ex(a, b):
# #     return a-b # 오름차순 정렬 의미
# #     return b-a # 내림차순 정렬 의미

# 2026/10/15
def solution(numbers):
    numbers = sorted(numbers, reverse=True, key=lambda x:str(x)*3)
    
    answer = ''.join(map(str, numbers))
    if (set(answer) == {'0'}):
        answer = '0'
        
    return answer
