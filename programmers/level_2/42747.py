# 42747
# H-Index

###
### sol1)
### 일종의 누적합으로 구하기
### 단, H-Index는 논문의 전체 개수보다 작을 수 밖에 없다는 사실!
# from collections import defaultdict

# def solution(citations):
#     c_cnt = defaultdict(int)
#     for cit in sorted(citations, reverse=True):
#         c_cnt[cit] += 1
    
#     ssum = 0
#     for h in reversed(range(10001)):
#         if (h in c_cnt):
#             ssum += c_cnt[h]
#         if (ssum >= h):
#             return h



###
### sol2) h_index는 최대 n (=논문 전체 개수)
### 더 깔끔 and faster.
def solution(citations):
    citations.sort()
    for h_idx in range(len(citations)):
        if (citations[h_idx] >= len(citations)-h_idx):
            return len(citations)-h_idx
    return 0
