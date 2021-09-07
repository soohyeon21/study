# 2163

n, m = map(int, input().split())

# 가로 금 (n - 1)개
# 세로 금 (m - 1)개

# 가로로 다 자르기
cut = n - 1
# 가로 조각 자르는 횟수 (m - 1)번 * 전체 가로 조각 수
cut += ((m - 1) * n)

print(cut)
