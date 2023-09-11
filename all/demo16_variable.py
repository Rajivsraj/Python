"""
a = 100

def total():
    print(a)    # r s n - no

total()
"""


"""
a = 100
def total():
    x = 20

total()
print(x)    ## n - y (wrong), s r - no
"""

"""
a = 100
def total():
    a = 20
    print(a)

total()     # n r s - 20,
"""

"""
a = 100
def total():
    # a = 200
    global x    # it can be access outside the function
    x = 200
    print(a)

total()     # n r s - 20,

print(x)
"""
