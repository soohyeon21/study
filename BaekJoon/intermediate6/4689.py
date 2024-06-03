# 4689

# except EOFError를 사용하면 ValueError 발생
# num, base_from, base_to = sys.stdin.readline().split()에서 error

# f"{'ERROR':>7s}" # 7칸 기준 오른쪽 정렬
# string.rjust(7)  # 7칸 기준 오른쪽 정렬

# .rjust(), .ljust(), .center() # 자매품

import sys

def convert(num, base):
    result = ""
    while (num != 0):
        result = convert_dict[num%base] + result
        num //= base
    return result


convert_dict = {i:str(i) for i in range(10)}
for j in range(10, 16):
    convert_dict[j] = chr(55+j)

while (1):
    try:
        num, base_from, base_to = sys.stdin.readline().split()
        
    except:
        break

    num10 = int(num, int(base_from))
    converted_num = convert(num10, int(base_to))
    if (len(converted_num) > 7):
        print(f"{'ERROR':>7s}")
    else:
        print(f"{converted_num:>7s}")
