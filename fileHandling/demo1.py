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
f = open("two.txt", "w")
f.write("Hello my first line\n")
f.write("This is my 2nd line")
f.close()

# overwite all the data of file
f = open("two.txt", "w")
f.write("2nd time writing\n")
f.write("This is my 2nd line")
f.close()