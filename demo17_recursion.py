import sys
# print(sys.getrecursionlimit())
sys.setrecursionlimit(2000)
"""i = 0
def recursion():
    global i
    i = i+1
    print("hello recursion",i)
    recursion()

recursion()"""

"""
i = 0
def recursion():
    global i
    global c
    i = i+1
    if i > 5:
        c = i
        return 0

    recursion()

x = recursion()
print(x)"""


"""
i = 0
def recursion():
    global i
    i = i+1
    if i > 5:
        return 0

    recursion()

recursion()
print(i)
"""



def recursion(no):
    if no == 0:
        return 0
    return no * recursion(no - 1)


print(recursion(5))

