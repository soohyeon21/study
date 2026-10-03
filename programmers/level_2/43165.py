# 43165
# 타겟 넘버

## 생각 flow
# 그럼 정리해보자면, 일단 이 문제는 모든 경우의 수를 따져봐야 하는 문제이고, 그 과정이 마치 tree처럼 그려지는데다가, 옆으로 가면서 찾 는게 아니라 각각의 끝을 보고 조건 즉 target값을 만족해야하는지 확인해야 하기 때문에 dfs를 사용한 풀이가 적절한거지
# 그리고, dfs(0, 0)으로 시작해서, dfs(현재 위치, 현재까지의 합)을 확인할 수 있도록 dfs를 구성하고, 재귀에 가장 중요한 종료조건을 명시 해서 dfs 종료를 먼저 정해주고, 거기서 걸러지지 않는 경우에는 그 다음 단계 그러니까 그 다음 깊이의 tree를 확인할 수 있도록 하고, cnt 를 사용할 수도 있지만, 그냥 0, 1, 각 값을 return 하도록 해서 그냥 Solution()자체에서 해결할 수 있게 하는거구나.

## global cnt를 쓰고 싶다면, 완전히 solution() 밖에 지정해야 함. 그러나 함수를 여러번 실행하는 과정에서 이전 값이 그대로 남아 있어 누적되는 문제가 발생하기 때문에, 코테에서는 사용을 추천하지 않음.



###
### sol1) solution()에서 바로 dfs(0, 0) return하기
###
# def solution(numbers, target):
#     def dfs(idx, total_sum):
#         if (idx == len(numbers)):
#             if (total_sum == target):
#                 return 1
#             return 0
#
#         value = dfs(idx+1, total_sum + numbers[idx]) + dfs(idx+1, total_sum - numbers[idx])
#         return value
#
#     return dfs(0, 0)



###
### sol2) cnt=[0] 활용하기
### list는 mutable 객체로, 메모리 주소가 고정되어 있음. 따라서 객체 자체는 그대로 두고 안의 값만 바꿔 사용하는 개념.
### 정수형 변수는 immutable 객체로, 새로운 메모리 공간을 할당하려고 하기 때문에, 바깥에 있는 변수를 그냥 수정하려고 하면 에러 발생. '이거 어디 있는 변수야?' 하면서.
###
# def solution(numbers, target):
#     cnt = [0]
#     def dfs(idx, total_sum):
#         if (idx == len(numbers)):
#             if (total_sum == target):
#                 cnt[0] += 1
#             return
#         dfs(idx + 1, total_sum + numbers[idx])
#         dfs(idx + 1, total_sum - numbers[idx])
#    
#     dfs(0, 0)
#     return cnt[0]



###
### sol3) nonlocal cnt 사용하기
### nonlocal # 해당 함수 바로 바깥에 정의된 cnt 가리켜줌.
###
def solution(numbers, target):
    cnt = 0
    def dfs(idx, total_sum):
        nonlocal cnt # dfs() 바로 바깥에 정의된 cnt 의미
        if (idx == len(numbers)):
            if (total_sum == target):
                cnt += 1
            return
    
        dfs(idx + 1, total_sum + numbers[idx])
        dfs(idx + 1, total_sum - numbers[idx])
    
    dfs(0, 0)
    return cnt
