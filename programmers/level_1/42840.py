# 42840
# 모의고사

# answers에 대해 %를 이용해서 1~3번 수포자의 답안과 비교하는 방법도 있음.

def solution(answers):
    math_pattern = [[1, 2, 3, 4, 5],
            [2, 1, 2, 3, 2, 4, 2, 5],
            [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    for k in range(3):
        math_pattern[k] = math_pattern[k]*(10000//len(math_pattern[k]))
    
    cnt = {1:0, 2:0, 3:0}
    for i in range(len(answers)):
        for student in range(3):
            if (answers[i] == math_pattern[student][i]):
                cnt[student+1] += 1
    
    answer = []
    for suposa in range(1, 4):
        if (cnt[suposa] == max(cnt.values())):
            answer.append(suposa)
    
    return answer
