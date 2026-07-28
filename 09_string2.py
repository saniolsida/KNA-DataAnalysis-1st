# email = "songsan@gmail.com"

# at = email.index("@")
# print(at)

# sqe = "SQE-00Q8"

# print(sqe[: sqe.find("-")])
# print(sqe[: sqe.index("-")])

# print(sqe.index("-"))

# EQP = "EQP-001"
# eqp = "EQP"

# print(EQP.startswith(eqp))

# sensor = "sensor_log.csv"
# print(sensor.startswith("sensor"))
# print(sensor.endswith(".csv"))

# endswith, len의 차이는?
# endswith는 메서드
# len은 함수

# str = "helloworld"
# str.upper
# print(str.upper)
# print(str.upper())

# ready = "ready"
# READY = ready.upper()
# print(READY)

# WARNING = "WARNING"
# warning = WARNING.lower()
# print(warning)

# name = "songsan songsan"
# print(name.capitalize())
# print(name.title())

# print("ABC".isupper())
# print("abc".islower())
# print("Abc".isupper())

# file = "Sensor_LOG.CSV"
# newFile = file.lower()
# print(newFile.startswith("sensor"))
# print(newFile.endswith("csv"))

# a = "  python"
# print(a[0:2] + "T" + a[3:])
# a = a.strip()
# a = a[:2] + a[2].upper() + a[3:]
# a = a.replace(a[2], a[2].upper())

# print(a)

# str1 = "===wj=== dtk==="
# str1 = str1.strip("=")
# print(str1)

# str = "    Warning    "
# print("[" + str.lower() + "]")
# print("[" + str.strip().lower() + "]")

# str = "   aabbbcc 이렇게? cd"
# str = str.strip("dc ")
# print(str)

# fruits = "apple, banana, grape, watermelon"
# fruits_list = fruits.split(", ")
# print(fruits_list)

# data = "a,b,c,d"
# data_list = data.split(",")
# print(data_list)
# data_list = "-".join(data_list)
# print(data_list)

# list = ["2025", "01", "15"]
# print("-".join(list))

# python = "python"
# # pyThon = python[:2] + python[2].upper() + python[3:]

# print("T".join(python.split("t")))

# print("2026", "7", "27", sep="love", end="A")

# date = "2025/01/15"
# newDate = "-".join(date.split("/"))
# print(newDate)

# data = "1, NORMAL ,25.3"
# index = data.split(",")
# index[1] = index[1].strip().lower()
# print(index[1])

# temp = 87
# id = "PUMP_A"
# print(f"설비 {id}, 온도 {temp}도")

# print(f"{18 * 2}")

# value = 87.456
# print(f"{value:.1F}")
# print(f"{value:.2F}")

sentence = " 5, sensor_2, WARNING , 0.78912 "
sentence = sentence.strip()
list = sentence.split(",")
temp = int(list[0].strip())
sens = list[1].strip()
state = list[2].strip().lower()
value = float(list[3].strip())
print(f"[센서 {sens}] 상태 {state}, 측정값 {value:.2f}")
