# def sum1():
#     print("Function")
#     def inner():
#         print("Inner function")
#     inner()
#
# sum1()


# def sum1():
#     print("Function")
#     def inner():
#         print("Inner function")
#         def inner1():
#             print("Inner 2")
#         return inner1
#     return inner
#
#
# x = sum1()
# y = x()
# y()

# lambda without arg
# abc = lambda: "hello"
# print(abc())

# lambda with args
# abc = lambda x: x
# print(abc(100))

# with 2 args
# abc = lambda x, y: x+y
# print(abc(100, 200))

# nested lambda
# abc = lambda x: lambda y: x+y
# xyz = abc(10)
# print(xyz(20))

# mul = lambda x: lambda y: x*y
# x = mul(10)
# print(x(100))
# print(mul(10)(20))    # short


# def mul(a):
#     return lambda: "hello"
# x = mul(10)
# print(x())

# def mul(a):
#     return lambda y: a+y
#
# x = mul(100)
# y = x(10)
# print(y)


# def mul(a):
#     # return a(100)
#     return a
#
# # x = mul(lambda x: x)
# # print(x)
# # print(x(100))


# def mul(a, b):
#     # return a(100)
#     return a(100)+b(200)
#
#
# x = mul((lambda x: x), (lambda x: x))
# print(x)


# IIFE (Immidiate Invoked function expression)
print((lambda x: x)(10))
