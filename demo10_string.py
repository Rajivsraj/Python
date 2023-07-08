# string = "Shatrughan"
# print(string)
# print(string[0])
# print(string[1])


# string = "Shatrughan"
# for x  in string:
#     print(x)

"""
# get only 4 chars
string = "Shatrughan"
for x  in range(4):
    print(string[x])
"""



# 29/06/2023 range()
"""for x in range(-10, -1):
    print(x)
else:
    print("Done")
"""


"""for x in range(2, 10, 2):
    print(x)
else:
    print("Done")"""


"""for x in range(10, 1, -1):
    print(x)
else:
    print("Done")"""


"""for x in range(10, 1, -1):
    print(x)
else:
    print("Done")"""


"""string = "Shatrughan"
char = string[0:4]
print(char)"""

"""
string = "Shatrughan"
char = string[:4]
print(char)
"""

"""
string = "Shatrughan"
char = list(string[:])
print(char)
"""


# string = "Shatrughan"
# char = string[0:]
# char = string[:]
# char = string[0:10:1]

# char = string[0:10:2]   # Sarga
# char = string[::2]   # Sarga

string = "Shatrughan"
# char = string[-1:-10]   #""
# char = string[-1:0]   #""

# char = string[-1:-11: -1]   #"nahgurtahS"
# char = string[-1]   #"n"
# char = string[-10]   #"S"
# char = string[:-4]   #"Shatru"
# char = string[:-4:-2]   #"S"
# print(char)


# rev = string[::-1]
# print(rev)


# STRING
"""
name = "Hello mohan how " \
       "are you"
# name = 'mohan'

# mutiple line string
namem = "hello hi" \
        "how are you"
# print(name)
print(namem)"""


# multiple line string
'''
name = """ 1st line
    hello first line
    2nd line
    3rd line
                lsdf
last line """
'''
"""
name = ''' 1st line
    hello first line
    2nd line
    3rd line
                lsdf
last line '''
"""
# print(name)

# Immutalbe
"""
name = "rahul"
name[0] = "k"   # not possible
name = "sohan"
print(name)"""


# repeat the sting
"""
name = "neetu"*2
print(name)
"""


# Concatenate
"""
fname = "neetu"
lname = "singh"
fullname = fname+lname
print(fullname)
"""

"""
name = "mohan "
extra = name*2+"hi"
print(extra)
"""


# string format (with current version)
"""name = "sohan"
age = 20

# f-string
print(f"my name is {name} and my age is {age}")

# c-style
print("my name is %s and my age is %d" %(name, age))

# string format method
print("my name is {} and my age is {}".format(name, age))
print("my name is {1} and my age is {0}".format(name, age))
"""

name = "mohan"
# print(name.capitalize())
# print(name.upper())
# print("sohan".upper())
"""
name = "MOHAN"
if name.isupper():
    print("mohans's initial letter is capital")
    print(name.isupper())
else:
    print("mohan's initial letter in not capital")
    print(name.isupper())
"""

"""
name = "  sohan"
print(name)
print(name.lstrip())
"""

name = " mohan "
print(name)
print(name.strip())
"""
capitalize()
upper()
lower()     - TYS
isupper()
islower()   - TYS
lstrip()
rstrip()    - TYS
strip()
replace() - TYS
endwidth() - YTS
rjust() - TYS
ljsut() - TYS
center() - TYS
"""

# conversion of letters to ascii code
"""
char = "a"
print(ord(char))

# conversion of ascii to letter
ascii = 97
print(chr(ascii))
"""
