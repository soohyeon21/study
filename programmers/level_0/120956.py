# 120956
# 옹알이 (1)

def solution(babbling):
    for i in range(len(babbling)):
        for word in ["aya", "ye", "woo", "ma"]:
            babbling[i] = babbling[i].replace(word, ' ')
    
    answer = 0
    for each in babbling:
        if (each.strip() == ''):
            answer += 1
    return answer
