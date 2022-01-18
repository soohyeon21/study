# 9654

# ㅋㅋ 그냥 복붙 형식으로 해도 되었네.

name = ["SHIP NAME", "CLASS", "DEPLOYMENT", "IN SERVICE"]
ship = ["N2 Bomber", "J-Type 327", "NX Cruiser", "N1 Starfighter", "Royal Cruiser"]
classs = ["Heavy Fighter", "Light Combat", "Medium Fighter", "Medium Fighter", "Light Combat"]
deplo = ["Limited", "Unlimited", "Limited", "Unlimited", "Limited"]
service = [21, 1, 18, 25, 4]

print("%-15s%-15s%-11s%-10s" %(name[0], name[1], name[2], name[3]))
for i in range(5):
    print("%-15s%-15s%-11s%-10d" %(ship[i], classs[i], deplo[i], service[i]))
