# 181829
# 이차원 배열 대각선 순회하기

def solution(board, k):
    answer = 0
    for i in range(k+1):
        for j in range(k+1):
            try:
                if (i+j <= k):
                    answer += board[i][j]
            except IndexError:
                continue
    return answer
