# print(2**3)

# # 산술연산자
# print(3 // 3)
# print(3 / 3)
# print(3 % 3)
# #
# # 방법 1) , 사용
# print("안녕", "하세요")
# # 안녕 뒤에 공백 추가
# print("안녕 " + "하세요")
# # 공백만 있는 문자열 더하기

# print("안녕" + " " + "하세요")
# print("heelo" * 5)

# < > <= >=

# print(3 < 7)
# print(3 == 3)
# print(3 != 5)
# print("hello" == "hello")
# print("hi" > "hello")

# 질문 1) hello 변수에 할당하는 값을 따옴표로 감싸지 않고 비교
# print("=== 질문 1) hello 변수에 할당하는 값을 따옴표로 감싸지 않고 비교 ===")
# hello = hi
# print(hello == hi)  # NameError(선언하지 않은 이름 호출했을 때)
# hi는 따옴표에 감싸져있지 않기 때문에 변수로 취급됨
# 그런데 우리는 hi 변수를 선언한 적이 없기 때문에 에러

# 실습 03
# a = True
# b = False
# print(a == b)
# print(a < b)
# print(a <= b)
# print(a >= b)
# print(a > b)
# print(a != b)

# # 실습 04

# temper = 85
# pressure = 5

# temper_true = temper >= 60 and temper <= 90
# print(temper_true)
# pressure_true = pressure >= 3 and pressure <= 7
# print(pressure_true)
# print(temper_true and pressure_true)

# 05
# item = 100
# print(item)
# item += 50
# print(item)
# item -= 30
# print(item)
# item += 5
# print(item)

# total = 500
# defect = 23
# per = (defect / total) * 100
# print(per, "%")

# total_time = 24
# oper_time = 21
# per_t = (oper_time / total_time) * 100
# print(per_t, "%")

total = 500
hour = (int)(500 / 60)
minute = 500 % 60

print(hour, "시간", minute, "분")
