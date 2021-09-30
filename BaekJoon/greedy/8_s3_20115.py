# 20115 에너지 드링크

# ver.1
# 오름차순으로 정렬하여 [-1]에 0번째 요소를 /2 해서 더해주는 것을 반복
# 더한 후에는 0번째 요소 remove로 제거

# ver.2
# 동일 아이디어 이지만, 이번에는 remove하지 않고 variable에 더했다.

# remove()를 시용하면 단순 variable을 사용했을 때보다 시간이 오래 걸리더라.

# ver.1
# remove() 사용 풀이
# 메모리: 40768 KB, 시간: 1964 ms, 코드 길이: 171 B
n = int(input())
vol = list(map(int, input().split()))

vol2 = sorted(vol)

for _ in range(n - 1):
    vol2[-1] += vol2[0] / 2
    vol2.remove(vol2[0])
    
print(vol2[0])

# ver.2
# variable 사용
# 메모리: 40768 KB, 시간: 132 ms, 코드 길이: 161 B
n = int(input())
vol = list(map(int, input().split()))

vol2 = sorted(vol)
value = vol2[n - 1]

for i in range(n - 1):
    value += vol2[i] / 2
    
print(value)
