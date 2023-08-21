# File Types
# text file    - decode
# Binary File - raw file : pdf, word, image, video
"""
# FIle Open
f = open("one.txt", "r", encoding="UTF8")

# Data Read
# Read 10 chars only
res = f.read(10)
print(res)

# Again Read 10 chars only from 10th character because we have already read 10 chars in above line
res2 = f.read(10)
print(res2)

f.close()"""



"""
# FIle Open
f = open("one.txt", "r", encoding="UTF8")

# Read whole file at once
res = f.read()
print(res)

f.close()"""



# Write in file
"""
f = open("two.txt", "w")
f.write("Hello my first line\n")
f.write("This is my 2nd line")
f.close()

# overwite all the data of file
f = open("two.txt", "w")
f.write("2nd time writing\n")
f.write("This is my 2nd line")
f.close()
"""

"""
f = open("three.txt", "r+")

data = f.read(2)
print(data)
f.write("third content")
f.seek(10)
data = f.read(10)
print(data)
"""


"""
f = open("four.txt", "r")
line = f.readline()
print(f.readline())
print(line)
"""


"""f = open("four.txt", "w")
f.write("hello line\n")
f.write("2nd line")
f.close()

f = open("four.txt", "rb")
data = f.read()
print(data)
f.close()
"""

"""f = open("four.txt", "r");
x = f.readline(5)
print(x)"""

"""
f = open("four.txt", "r")
x = f.readlines()   # without arg
x = f.readlines(17)
print(x)"""

f = open("four.txt", "w+")
f.write("hi")
