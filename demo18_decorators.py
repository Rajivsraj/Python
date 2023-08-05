# decorator is a function that accept a function as an argument
# decorator is used to modfiy existing functionality of a function with modify the original method
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


print(total())