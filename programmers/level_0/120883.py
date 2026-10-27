# 120883
# 로그인 성공?

def solution(id_pw, db):
    answer = 'fail'
    
    for did, dpw in db:
        if (id_pw[0] == did):
            if (id_pw[1] == dpw):
                answer = 'login'
            else:
                answer = 'wrong pw'
    
    return answer
