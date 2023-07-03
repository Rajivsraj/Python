import array


"""marks = array.array("i", [10, 50, 64, 73, 64])
print(marks[0])
print(marks[1])
print(marks[2])
"""


"""
marks = array.array("i", [10, 50, 64, 73, 64])
for x in marks:
    print(x)
"""

# print all the elements using while loop

"""from array import *
marks = array("i", [53, 64, 64, 354, 45])
print(marks[0])"""
# print all elements using for loop and while loop


"""
import array as arr
marks = arr.array("i", [43, 45, 654, 34])
# n = len(marks)
for x in range(len(marks)):
    print(marks[x])
"""

from array import *
# creating blank array

"""marks = array("i", [])
print(marks)
marks[0] = 50
print(marks)"""


"""marks = array("i", [])
print(marks)
marks.append(40)
marks.append(60)
print(marks)

marks[0] = 100
print(marks)
"""

# get value from  user and store it into array

"""marks = array("i", [])
val = int(input("Enter a value: "))
marks.append(val)
print(marks)"""

"""
marks = array("i", [])
marks.append(int(input("Enter a value: ")))
print(marks)
"""

"""
marks = array("i", [])
size = int(input("Enter how many elm you want to store: "))

for x in range(size):
    marks.append(int(input("Enter element at ")))

print(marks)"""
# accept value untill user don't want to store more values


# marks = array("i", [10, 45, 34, 63, 74, 10, 73])
# marks.insert(2, 100)
# x = marks.pop()
# x = marks.pop(2)
# print(x)
# marks.remove(10)
# print(marks)
# 1. remove given value form the array (all values)

"""marks = array("i", [10, 45, 34, 63, 74, 10, 73])
marks2 = array("i", [100, 200])
# x = marks.index(34)
# marks.reverse()
marks.extend(marks2)
# print(x)
print(marks)"""