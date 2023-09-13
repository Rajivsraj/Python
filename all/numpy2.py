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
# a1 = array([10, 20, 300, 140, 50])
# a2 = array([10, 40, 40, 120, 500])
# a3 = a1 == a2
#
# print(any(a1 == a2))
# print(all(a1 == a2))
#
# print(a3)




# a1 = array([10, 20, 300, 140, 50])
# a2 = array([10, 40, 40, 120, 500])
#
# res = a1==a2


#
# a1 = array([10, 20, 300, 140, 50])
# a2 = array([11, 40, 40, 120, 500])
# res = a1>a2
#
# # x = where(res, "ok", "not")
# x = where(res, a1, a2)
# print(x)


# a1 = array([10, 20, 300, 0, 140, 50, 0, 100])
# res = nonzero(a1)
# print(res)

#
# a1 = array([10, 20, 300, 0, 140, 50, 0, 100])
# a2 = a1
# a3 = a1
#
# print(a1, id(a1))
# print(a2, id(a2))
#
# a1[2]=222
#
# print(a1)
# print(a2)



#
# a1 = array([10, 20, 300, 0, 140, 50, 0, 100])
# a2 = a1.view()
#
# print(a1, id(a1))
# print(a2, id(a2))
#
# a2[2]=333
# a1[3] = 333333
#
# print(a1)
# print(a2)






# a1 = array([10, 20, 300, 0, 140, 50, 0, 100])
# a2 = a1.copy()
#
# print(a1, id(a1))
# print(a2, id(a2))
#
# a2[2]=333
# a1[3] = 333333
#
# print(a1)
# print(a2)


#
# no = 20
# temp = no
# print(no, temp)
#
# no = 100
# print(no, temp)



# a1 = array([10, 20])
# a2 = a1
#
#
# print(a1, id(a1), a2,  id(a2))
# a2[0] = a2[0]+1
# a2[1] = a2[1]+1
#
#
# print(a1, a2)



# a1 = array([10, 20, 300, 0, 140, 50, 0, 100])
# res = reshape(a1, (4, 2))
# res = reshape(a1, (1, 8))

# print(res)



# a1 = array([10, 20, 300, 0, 140, 50, 0, 100])
# res = reshape(a1, (2, 2, 2))
# print(res)


# a1 = array([[10, 20, 300, 0], [140, 50, 0, 100]])
# print(a1.ndim)

a1 = array([10.21, 20, 300, 0, 140, 50, 0, 100])
print(type(a1))
print(a1.shape)
print(a1.size)
print(a1.itemsize)
