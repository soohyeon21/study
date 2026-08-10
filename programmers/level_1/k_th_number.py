# K번째수

def solution(array, commands):
    answer = []
    for command in commands:
        cut = sorted(array[command[0]-1:command[1]])
        answer.append(cut[command[2]-1])
    return answer
