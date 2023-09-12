from numpy import *

# a1 = linspace(1, 8)
# a1 = linspace(1, 8, num=16)
# a1 = linspace(1, 8, num=8, dtype=int)
# print(a1)

# print(a1[2])
# print usng while and for


# x = logspace(1, 5, 5)   # 10**1  10**2 3**10 10**4, 10**5
                            # 10  100  1000
# x = logspace(1, 5, 5, base=20)
# print(x)

# ARANGE
# x = arange(1, 8, 8)
# print(x)


# a1 = zeros(10, dtype=int)

# a1 = ones(10, dtype=int)

# print(a1)


# a1 = array([[10, 20, 30, 40], [90, 54, 56, 45]], dtype=int)

# a1 = array([["Rahul", "sumit"], ["Mohan", "Sohan"]], dtype=str)
# a1 = array(["hello", 2
# 0, 345.45])
# a1 = array(["hello", "hi", "shatrughan"])
# a1 = array([10.12, 20.0, 30.20])
# print(a1.dtype)
# print(type(a1))
# print(a1)

# a1 = array([10, 20, 30, 40])
# res = a1 + 5
# print(res)

#
# a = [10, 20, 30, 40, 50, 60, 79]
# b = [1, 2, 3, 5]
#
# if len(a) == len(b):
#     a1 = array(a)
#     a2 = array(b)
# elif len(a) > len(b):
#     print("both not equal")
#     dif = len(a) - len(b)
#     print(dif)
#     for x in range(1, dif+1):
#         b.append(0)
#
# print(a, b)
#
# a1 = array(a)
# a2 = array(b)
# res = a1 + a2
# print(res)

# a1 = array([10, 20, 30, 40, 50])
# a2 = array([10, 20, 40, 40, 50])
# # a3 = a1 == a2

# a1 = array([10, 20, 300, 140, 50])
# a2 = array([10, 40, 40, 120, 500])
# a3 = a1 > a2
# print(a3)

# any() all()
a1 = array([10, 20, 300, 140, 50])
a2 = array([10, 40, 40, 120, 500])
a3 = a1 == a2

print(any(a1 == a2))
print(all(a1 == a2))

print(a3)