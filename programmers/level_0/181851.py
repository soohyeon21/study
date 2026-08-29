# 181851
# 전국 대회 선발 고사

# True인 학생만 student에 넣는 방법도 있음.

def solution(rank, attendance):
    student = [(i, rank[i], attendance[i]) for i in range(len(rank))]
    student.sort(key=lambda x:(x[2], -x[1]), reverse=True)

    result = 10000*student[0][0] + 100*student[1][0] + student[2][0]
    
    return result
