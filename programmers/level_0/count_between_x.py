# x 사이의 개수

def solution(myString):
    xsplit = myString.split('x')
    answer = [len(o) for o in xsplit]
    return answer
