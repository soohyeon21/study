# 42746
# 가장 큰 수

# 35 > 34 > 3 > 32 > 31 > 30
# 46 > 45 > 4 > 43 > 42 > 41 > 40

# numbers.sort(key=lambda x:x*3, reverse=True)
# 문자열 비교이기 때문에, '333' vs '343434' vs '354354354' (3, 34, 354) 비교가 가능하다! 어차피 사전식(lexicographic) 비교이기 때문.

# python 3.11 이상: int() 4300자리로 제한.

# sort에서 key는 원소당 한 번만 계산되기 때문에 빠르고,
# cmp_to_key는 비교할 일이 있을 때마다 compare()를 호출하기 때문에 비교적 느림.
# 비교 함수가 정의된 객체를 만들어주는 cmp_to_key(compare)
# compare() 역할: 비교할 때 어떤 기준으로 비교할건지.

###
### sol1) sort_key_lambda_x*3
###
# def solution(numbers):
#     numbers = list(map(str, numbers))
#     numbers.sort(key=lambda x:x*3, reverse=True)
    
#     answer = ''.join(num for num in numbers)
#     if (answer[0] == '0'):
#         answer = '0'
    
#     return answer


###
### sol2) functools.cmp_to_key(compare)
###
from functools import cmp_to_key

def compare(a, b):
    if (a+b > b+a):
        return -1
    elif (a+b < b+a):
        return 1
    else:
        return 0

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=cmp_to_key(compare))
    
    answer = ''.join(num for num in numbers)
    if (answer[0] == '0'):
        answer = '0'
    
    return answer
