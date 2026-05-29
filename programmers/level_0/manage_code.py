# 코드 처리하기

def solution(code):
    mode = 0
    ret = ''
    for i in range(len(code)):
        if (code[i] == '1'):
            mode = (mode+1)%2
        else:
            if (mode == 0):
                if (i%2 == 0):
                    ret += code[i]
                
            elif (mode == 1):
                if (i%2 == 1):
                    ret += code[i]
    
    if (ret == ''):
        ret = 'EMPTY'
        
    return ret
