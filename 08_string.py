# notice = """
#     설비 점검 안내
#     1. 전원 확인
#     2. 센서 점검
# """

# print(notice)

name = "PUMP_A"
state = "정상"
act = 1200
date = "2026-07-16"

card = "설비: " + name + "\n상태: " + state + "\n가동: " + str(act) + "\n점검: " + date
print(card)
