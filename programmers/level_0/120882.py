# 120882
# 등수 매기기

def solution(score):
    pair = sorted([(sum(score[idx])/2, idx) for idx in range(len(score))], reverse=True)
    
    lineup = [(1, pair[0][0], pair[0][1])]
    order = 1
    same = 0
    for i in range(1, len(score)):
        if (pair[i][0] != lineup[-1][1]):
            order += 1 + same
            same = 0
        else:
            same += 1
        lineup.append((order, pair[i][0], pair[i][1]))
    lineup.sort(key=lambda x:x[2])
    
    answer = [v1 for v1, v2, v3 in lineup]
    return answer
