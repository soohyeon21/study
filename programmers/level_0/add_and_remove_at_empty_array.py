# 빈 배열에 추가, 삭제하기

def solution(arr, flag):
    answer = []
    for i in range(len(flag)):
        if (flag[i]):
            answer.extend([arr[i]] * arr[i]*2)
        else:
            for k in range(arr[i]):
                answer.pop()
    return answer
