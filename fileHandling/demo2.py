"""
f = open("five.txt", "w")
print(f.readable())
print(f.writable())
"""

"""
f = open("five.txt", "r")
print(f.read())
print(f.seekable())
print(f.read())
print(f.seekable())
f.seek(0)
print(f.seekable()) """



"""
f = open("img.jpg", "r")
print(f.seekable())
print(f.seekable())
"""


#
# with open("five.txt", "r+") as f:
#     print(f.tell())
#     print(f.read(10))
#     lread = f.tell()
#     f.write("\nthis is 3rd line")
#     f.seek(lread)
#     print(f.read(10))
#     print(f.fileno())

#
# with open("one.txt", "r") as f:
#     print(f.fileno())
#     print(f.isatty())

"""
f = open("five.txt", "r", encoding="UTF-8")
print(f.name)
print(f.closed)
print(f.mode)
print(f.buffer)
print(f.encoding)
print(f.newlines)
"""


import os

"""
if os.path.isfile("five.txt"):
    f = open("five.txt", "r")
else:
    print("file not exists")"""


# print(os.getcwd())
# os.mkdir("software/python/f2")
# os.mkdir("software/python")
# os.chdir("software")
# print(os.getcwd())
# print(os.listdir("software"))

# os.mkdir("hello")
# os.rmdir("hello")
# os.remove("four.txt")

# os.rename("../conditional.py", "con.py")

f = "software"
lst = os.listdir(f)

for x in lst:
    if os.path.isdir(f+"/"+x):
        print(x)
        nlst = os.listdir(f+"/"+x)
        if len(nlst)!=0:
            print(nlst)


# print(nlst)

# x = os.listdir("software/python")
# print(x)

