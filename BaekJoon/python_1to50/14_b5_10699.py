# 10699

# from os import open
# os라는 namespace 이름을 주고 앞으로 open이라고만 이름을 사용하면
# 그게 곷 os 모듈의 것이라는 의미.
# or else, os.open()과 같이 모듈까지 지정해서 사용해야 함.

import datetime

lc = datetime.datetime.today().strftime("%Y-%m-%d")
print(lc)

# same code
##from datetime import datetime
##
##lc = datetime.today().strftime("%Y-%m-%d")
##print(lc)
