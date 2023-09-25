# 12:00 - 12:30 : 22/09/2023
import re

st = "Hello World"

st = re.split("\s", st)
print(" ".join(st[::-1]))
