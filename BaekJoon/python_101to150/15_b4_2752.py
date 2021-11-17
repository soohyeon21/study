# 2752

# sort()는 리스트명.sort( ) 형식으로 "리스트형의 메소드"​​이며 리스트 원본값을 직접 수정합니다.
# sorted()는 sorted( 리스트명 ) 형식으로 "내장 함수"이며 리스트 원본 값은 그대로이고 정렬 값을 반환합니다.

num = list(map(int, input().split()))

num.sort()

n = str(num[0])
for i in range(1, 3):
    n += (" "+str(num[i]))

print(n)
