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

hi = "hello"
print(hi == "hello")

# 질문 1) hello 변수에 할당하는 값을 따옴표로 감싸지 않고 비교
# print("=== 질문 1) hello 변수에 할당하는 값을 따옴표로 감싸지 않고 비교 ===")
# hello = hi
# print(hello == hi)  # NameError(선언하지 않은 이름 호출했을 때)
# hi는 따옴표에 감싸져있지 않기 때문에 변수로 취급됨
# 그런데 우리는 hi 변수를 선언한 적이 없기 때문에 에러

# 질문 1) 해결방법
# print("=== 질문 1) 해결 방법 ===")
hi = "안녕"  # hello 변수에 hi 변수를 할당하기 전 hi 변수 선언
hello = hi  # print(hello) > 안녕
print("=== 변수 hello(안녕)와 변수 hi(안녕) 비교 ===")
print(hello == hi)  # True
