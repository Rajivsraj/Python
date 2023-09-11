# import numpy
# numpy.array(object, dtype=None, copy=True, order='K', subok=False, ndmin=0)

# a1 = numpy.array([10, 20, 30, 40])
# a1 = numpy.array([10, 20, 30, 40], int)
# a1 = numpy.array([10, 20, 30, 40], dtype=int)
# a1 = numpy.array(["Rahul", "sumit", "amit"], dtype=str)
#
# print(a1)
# print(a1.dtype)


import numpy

# # numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)
# start: starting element
# end: ending element
# num: shows num of parts the element should be divided. Default is 50. It must be non-negative
# endpint: If true, include last/stop element else will not include


# from numpy import *
#
# # linspace(start, end, num=50, endpoint=Ture)
#
# x = linspace(1, 5)
# x = linspace(1, 10, num=5)
# x = linspace(1, 10, 5)
# print(x)






# LOGSPACE
# numpy.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None, axis=0)

# from numpy import *
#
# x = logspace(1, 5, 5)  #1'10, 5'10
# x = logspace(1, 5, 5, base=15)  #1'10, 5'10
# print(x)



#zeros()
# numpy.zeros(shape, dtype=float, order="C")
#
# from numpy import *
# x = zeros(5)
# x = zeros(5, dtype=int)
# x = zeros((3,3))    # 2d array
# print(x)



# #ones()
# # numpy.ones(shape, dtype=float, order="C|F")
#
# from numpy import *
# x = ones(5)
# x = ones(5, dtype=int)
# x = ones((3,3))    # 2d array
# print(x)


from numpy import *

# a1 = array([10, 20, 30, 40])
# add = a1+2
# print(add)


# a1 = array([10, 20, 30, 40])
# a2 = array([1, 2, 3, 44])
# add = a1+a2
# print(add)


# Comparision
# a1 = array([10, 20, 30, 40])
# a2 = array([1, 2, 30, 44])
# c = a1 == a2
# print(c)


# a1 = array([10, 20, 30, 40])
# a2 = array([1, 2, 30, 44])
# c = a1 == a2
# print(any(c))       # True



# a1 = array([10, 20, 30, 40])
# a2 = array([1, 2, 30, 44])
# c = a1 == a2
# print(all(c))       # False


# Where
# numpy.where(condition, exp1, exp2)
# a1 = array([10, 20, 30, 40])
# a2 = array([1, 2, 30, 44])
# res = where(a1>a2, a1, a2)
# res = where(a1>a2, "h1", "hello")
#
# print(res)       # [10 20 30 44]



# a1 = array([10, 20, 30, 40, 0, 35])
# res = nonzero(a1)
# print(res)


# a1 = array([10, 20, 30, 40, 0, 35])
# res = a1.view()
# print(a1, id(a1))   # [10 20 30 40  0 35] 2359655561424
# print(res, id(res)) # [10 20 30 40  0 35] 2359655562768



# a1 = array([10, 20, 30, 40, 0, 35])
# res = a1.copy()
#
# res[4] = 100
# print(a1, id(a1))   # [10 20 30 40  0 35] 1977970556720
# print(res, id(res)) # [ 10  20  30  40 100  35] 1977970556624



# a1 = array([
#     [10, 20, 30],
#     [70, 80, 90]
# ])
# print(a1)


a1 = array(
    [
        [
            [10, 20, 30],
            [20, 30, 40],
            [30, 40, 50]
        ]
    ]
)

print(a1)