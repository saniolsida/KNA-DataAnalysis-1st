# print("온도", 75)
# print("진동", 2.3)
# print("압력:", 4.0)

# 1.
#  File "/Users/songsan/Developer/Python/03_error.py", line 6
#     print("온도", 2.3
#          ^
# SyntaxError: '(' was never closed

# 2.
#   File "/Users/songsan/Developer/Python/03_error.py", line 11
#     print("진동", 2.3
#          ^
# SyntaxError: '(' was never closed

# 3.
#  File "/Users/songsan/Developer/Python/03_error.py", line 19
#     print("압력": 4.0)
#               ^
# SyntaxError: invalid syntax

print("온도", 75)
print("진동", 2.3)
print("압력:", 4.0)

print("=====", "1번", "설비 점검", "=====")
print("온도(˚C):" + "82")  # 정상온도 80
print("온도 상승량:", 11)
