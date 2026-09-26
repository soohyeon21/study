# 120913
# 잘라서 배열로 저장하기

def solution(my_str, n):
    answer = []
    for i in range(len(my_str)//n+1):
        tmp = my_str[i*n:(i+1)*n]
        if (tmp != ''):
            answer.append(tmp)
    return answer
