# 43165
# 타겟 넘버

# 이 풀이에서: 재귀 깊이는 N, 시간복잡도는 O(2**N)
def solution(numbers, target):
    cnt = [0]
    
    def dfs(now, total):
        if (now == len(numbers)): # 종료조건
            if (total == target):
                cnt[0] += 1
            return
            
        dfs(now+1, total + numbers[now])
        dfs(now+1, total - numbers[now])
    
    dfs(0, 0)
    return cnt[0]
