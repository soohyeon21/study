# pg.115 #1 왕실의 나이트

# 잘 풀기는 했다만,
# 앞으로를 위해서는 다른 방식으로 접근하는 방법을 배우는 게 좋을 것 같다.

at = input()

movea4 = ['b', 'g']
movei4 = [2, 7]
movea2 = ['a', 'h']
movei2 = [1, 8]
movea3 = ['a', 'b', 'g', 'h']
movei3 = [1, 2, 7, 8]

if (('c' <= at[0] <= 'f')and (3 <= int(at[1]) <= 6)):
    print(8)
elif ((at[0] in movea4) and (int(at[1]) in movei4)):
    print(4)
elif (('b' <= at[0] <= 'g')and (2 <= int(at[1]) <= 7)):
    print(6)
elif ((at[0] in movea2) and (int(at[1]) in movei2)):
    print(2)
elif ((at[0] in movea3) and (int(at[1]) in movei3)):
    print(3)
else:
    print(4)
