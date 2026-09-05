# 181844
# 배열의 원소 삭제하기

def solution(arr, delete_list):
    answer = []
    for each in arr:
        if (each not in delete_list):
            answer.append(each)
        
    return answer
