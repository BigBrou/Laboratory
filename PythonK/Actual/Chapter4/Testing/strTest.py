#Quiz 1
print("점프 투 파이썬")

#Quiz 2
str = """Life is too short
You need Python
"""
print(str)

#Quiz 3
print("%24s"%"PYTHON")

#Quiz 4
pregi = "890814-1111111"
lPregi = pregi[:6]
rPregi = pregi[8:]
print(lPregi, "----" , rPregi)

#Quiz 6
str6 = "1980M1120"
print(str6[4] + str6[:4] + str6[5:])

#Quiz7
str = "PYTHON"
print("{0:>24}".format(str))

#Quiz8
strings = "Life is too short, you need python"
print(strings.index("short"))

#Quiz9
str9 = "a:b:c:d"
strNew = str9.replace(":", "#")
print(strNew)

#Quiz10
print("------")
list = []
str10 = "a:b:c:d"
list = str10.split(":")
aspliter = "#"
print(aspliter.join(list))
