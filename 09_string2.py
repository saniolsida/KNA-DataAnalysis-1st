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

a = "python"
# print(a[0:2] + "T" + a[3:])

a = a[:2] + a[2].upper() + a[3:]
# a = a.replace(a[2], a[2].upper())

print(a)
