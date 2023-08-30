import re

str = """hello i am first \n line
hello I'm 2nd line
I'm third line"""

# x = re.findall("\d", str)
# x = re.findall("[0-9]", str)
# x = re.findall("[0-9]{2}", str)
# x = re.findall("^.", str)
x = re.findall("ne$", str)
print(x)
