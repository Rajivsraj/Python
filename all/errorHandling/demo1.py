"""a = 10
try:
    print(a)
except NameError:
    print("Variable not defined")"""

"""a = 10
b = 0

try:
    print(a/b)
except ZeroDivisionError:
    print("No can't be devide by 0")"""


# Handle all types of exception
"""try:
    print(a/b)
except:
    print("No can't be devide by 0")"""

"""a = 10
d = 10
try:
    print(a/d)
except NameError:
    print("Variable not defined")
except ZeroDivisionError:
    print("No can't be devided by 0")"""


"""a = 10
d = 0
try:
    print(a/d)
except (NameError, ZeroDivisionError):
    print("Variable not defined or divisor is 0")
"""

import time


"""
try:
    for x in range(5):
        print(x)
        time.sleep(1)
except:
    print("User Terminated the program")
"""

"""
try:
    for x in range(5):
        print(x)
        time.sleep(1)
    try:
        print(10/1)
    except ZeroDivisionError:
        print("divisor can't be 0")
except:
    print("User Terminated the program")
"""




"""
try:
    for x in range(5):
        print(x)
        time.sleep(1)
except:
    print("User Terminated the program")
else:
    print("will run if no exception occure")
finally:
    print("I'll execute always")"""


try:
    print(10/0)
except ZeroDivisionError as obj:
    print(obj)
