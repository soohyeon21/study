# 42584
# 주식가격

###
### so1) stack/queue 사용x. for()x2.
###
# def solution(prices):
#     answer = [0]*len(prices)
#     for i in range(len(prices)):
#         for k in range(i+1, len(prices)):
#             answer[i] += 1
#             if (prices[i] > prices[k]):
#                 break
#
#     return answer



###
### sol2) 기본적으로 max값을 고려하고, 만약 값이 떨어진 시점이 발생하면 그 시점을 처리하고 이어서 그 전 시점들까지도 확인하며(feat. stack) 처리하기.
###
def solution(prices):
    answer = [x for x in reversed(range(len(prices)))] # initial answer에는 best case인 경우의 값으로.
    
    stack = [0] # 처리할 index가 담김.
    for i in range(1, len(prices)):
        while (stack and (prices[stack[-1]] > prices[i])): # 만약 다음 sec에 가격이 떨어진 경우. # stack empty 확인 여부 필요함.
            change = stack.pop()
            answer[change] = i - change # 두 시점 사이 간격만큼이 answer값에 해당됨.
        stack.append(i)
    
    return answer
