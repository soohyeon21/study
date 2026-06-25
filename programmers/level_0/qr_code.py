# qr code

# code의 모든 index를 for문으로 일일이 확인하는 방법이 더 좋을까? # 문제에서 설명한 순서대로 풀이한 방법.
# code[r::q] # 시간 복잡도 상에서 더 좋은 방법.

def solution(q, r, code):
    answer = ''
    for i in range(len(code)//q+1):
        if (i*q+r < len(code)):
            answer += code[i*q+r]
    return answer
