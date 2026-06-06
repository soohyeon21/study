# 수열과 구간 쿼리 3

def solution(arr, queries):
    result = arr
    for query in queries:
        result[query[0]], result[query[1]] = result[query[1]], result[query[0]]
    
    return resul
