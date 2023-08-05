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