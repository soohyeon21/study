# 가까운 1 찾기

# index(list, 시작_index)

def solution(arr, idx):
    arr = list(map(str, arr))
    answer = ''.join(arr[idx:]).find('1')
    if (answer != -1):
        answer += idx
    
    return answer
