# 120862
# 최댓값 만들기 (2)

# or max(sorted[-1]*sorted[-2], sorted[0]*sorted[1])

def solution(numbers):
    answer = min(numbers) * max(numbers)
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer = max(answer, numbers[i]*numbers[j])
    return answer
