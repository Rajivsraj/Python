# decorator is a function that accept a function as an argument
# decorator is used to modfiy existing functionality of a function with modify the original method
"""
def dec(fun):
    def inner():
        fun()
        print("Rajiv modified display method")
    return inner

@dec
def display():
    print("Hello I'm display1")
    print("Hello I'm display2")
    print("Hello I'm display3")
    print("Hello I'm display4")


# display = decorator(display)
# print(type(display()))

display()


def total():
    return 10+20


print(total())"""

"""
def dec(fun):
    print(fun)
    def inner():
        print("Hi")
        fun()
    return inner

@dec
def show():
    print("Hello")


# x = dec(show)
# x()
show()
"""

lst = [45, 46, 72, 734,  66, 64]
def mul(no):
    return no*2

#
# x = map(mul, lst)
# print(x)
#
# for a in x:
#     print(a)


from functools import *
lst = [x for x in range(1,6)]
lst = [34,345,34,6,54,6,45]
print(lst)
def abc(a, b):
    return a*b

# x = reduce(abc, lst)
x = reduce(lambda a,b: a*b, lst)
print(x)

# reduce
# factorial
