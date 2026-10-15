# 42747
# H-Index

# 2026/10/15
def solution(citations):
    citations = sorted(citations)
    for h in reversed(range(max(citations)+1)):
        for i in reversed(range(len(citations))):
            if (citations[i] >= h):
                if (len(citations)-i >= h):
                    return h
    return 0 # 필요!
