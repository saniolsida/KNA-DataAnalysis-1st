# notice = """
#     설비 점검 안내
#     1. 전원 확인
#     2. 센서 점검
# """

# print(notice)

# name = "PUMP_A"
# state = "정상"
# act = 1200
# date = "2026-07-16"

# card = "설비: " + name + "\n상태: " + state + "\n가동: " + str(act) + "\n점검: " + date
# print(card)

# word = "PYTHON"
# print(word[0], word[3])

# abc = "abcdefghijklmnopqrstuvwxyz"

# name = abc[18] + abc[14] + abc[13] + abc[6] + abc[18] + abc[0] + abc[13]
# print(name)

# phone = "010-9191-4159"

# print(phone[-2:-5:-1])  # 시작은 포함, 끝은 포함 안됨

# word = "hello"

# print(word[:4])  # start 생략 0~4
# print(word[2:])  # end 생략 2~
# print(word[-5:])
# print(word[:999])  # 범위를 초과해도 오류를 넘어가지 않는다.

# word = "temp_sensor"
# print(word[:4])

# word = "temp_sensor"
# print(word[5:])

# word = "sensor_01"
# print(word[-2:])

# word = "PYTHON"
# print(word[::-1])

# word = "PYTHON"
# print(word[::2])

# var = "guys we only left 1 hour!"
# print(len(var))

# phone = "01012345678"
# print(len(phone))

# word = "고장12314"
# print("고장" not in word)

# print("고장" in "설비 고장 발생")
# print("정상" in "설비고장발생")

# print("설비에서 고장" not in "설비 고장 발생")
# print("설비에서 고장" in "설비 고장 발생")

# word = "banana"
# print(word.count("a"))

# word = "a,b,c,d"
# print(word.count(","))

word = "abcdefg"
print(word.find("d"))

email = "hong@company.com"
at = email.find("@")
user_id = email[:at]
print(user_id)
