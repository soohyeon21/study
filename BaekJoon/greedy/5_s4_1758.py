# 1758 알바생 강호

# list의 copy본을 만들고자 한다면
# list1 = sorted(list) # list1은 정렬된 list의 copy본
# list2 = list(reversed(list1)) # list2는 list1의 copy본
# 이렇게 해야 원본인 list에 영향을 주지 않는 새로운 리스트 list1, list2가 만들어진다.

# 오름차순으로 정렬한 뒤 0~(n-1)을 빼는 것과
# 내림차순으로 정렬한 뒤 0~(n-1)을 빼는 것 중에
# 무엇이 더 최대값을 만들지 몰라서 두 개 다 했는데,
# 다른 사람들은 내림차순만을 구현해 놓았다.
# 내림차순 case가 최댓값을 구하는 최선의 방법이라고 항상 확신할 수 있을까?

def cal_tip(case):
    hab = 0
    for j in range(n):
        val = case[j] - j
        if (val > 0):
            hab += val
    return hab

n = int(input())

tip = []

for i in range(n):
    tip.append(int(input()))

case1 = sorted(tip)
case2 = list(reversed(case1))


cases = []
cases.append(cal_tip(case1))
cases.append(cal_tip(case2))

print(max(cases))
