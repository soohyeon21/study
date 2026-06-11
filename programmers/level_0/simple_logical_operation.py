# 간단한 논리 연산

# 논리 연산(logical operation) # True, False 두 가지 원소만 존재하는 집합에서의 연산.
# and # &
# or # |

def solution(x1, x2, x3, x4):
    answer = (x1 or x2) and (x3 or x4)
    return answer
