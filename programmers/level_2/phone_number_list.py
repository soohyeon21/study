# 전화번호 목록

# Hash Map은 key-value 쌍으로 값을 저장하는 자료구조.
# 해싱 기반이기 때문에 탐색/삽입/삭제 시간복잡도 O(1).
# python에서는 dictionary.

# list에서 in # 평균 O(n)
# dict에서 in # 평균 O(1), 최악 O(n)
# set에서 in # 평균 O(1), 최악 O(n)

# str1.startswith(str2) # str1이 str2로 시작하는지 True or False
# zip() # 입력 iterable 자료형 간의 크기가 다를 경우, 부족한 만큼 None으로 채움.

def solution(phone_book):
    pset = set(phone_book)
    for phone in phone_book:
        ## sol1) slicing으로 조각 확인
        for i in range(1, len(phone)):
            if (phone[:i] in pset):
                return False
        
        ## sol2) 각 전화번호마다, 숫자 하나씩 더해가며 확인
        # tmp = ''
        # for digit in phone:
        #     tmp += digit
        #     if ((tmp in pset) and (tmp != phone)):
        #         return False
    return True
    
    # ## sol3) 틀린 풀이. 반례가 뭐가 있을까?
    # phone_book.sort()
    # for x1, x2 in zip(phone_book, phone_book[1:]):
    #     if (str(x2).startswith(str(x1))):
    #         return False
    #     return True
