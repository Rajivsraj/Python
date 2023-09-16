import pandas as pd
import numpy as np

# s = pd.Series([10, 20, 30, 40, 50, 60])

# lst = ["Rahul", "sumit", "amit"]
# s = pd.Series(lst)


# s = pd.Series([10, 20, 30, 40, 50, 60, "hi", 20.24])


# n = np.array([20, 30, 409, 50])
# s = pd.Series(n)


# st = {20, 30, 40, 50, 20, 60, 30}
# tpl = (20, 40, 60, 20, 90)
# s = pd.Series(tpl)
# print(s)
# s[0] = 100
# print(s[0])


# n = np.array([10, 20, 30, 40])
# s = pd.Series(n)
# print(s)
#
# for x in s:
#     print(x)


# s = pd.Series([10, 20, 30, 40])

# # Labeling / indexing
# s = pd.Series(data=[10, 20, 30, 40], index=["hindi", "english", "skt", "maths"])
#
# # print series
# print(s)
#
# # Access specific index value
# print(s["hindi"])
#
# # Print series using loop
# for x in s:
#     print(x)


# s = pd.Series(data=[10, 20, 30, 40], index=["h", "e", "m", "s"], dtype=int)
# print(s)
# print(type(s))

# z = np.zeros(10, dtype=int)
# print(z)


# s = pd.Series(29, index=[0, 1, 2, 3, 4])
# s = pd.Series(29, index=["one", "two", "three"])
# print(s)



# s = pd.Series([10, 20, 20, 40, 50, 60])
# print(s)


# s = pd.Series([10, 20, 30], index=["one", "two", "three"])
# print(s.index)


# s = pd.Series([10.0, 20.30, 20.64, 40.45, 5.50, 60.45])
# print(s)
# print(s.index)


# s = pd.Series([10, 20, 30], index=[3,2,1])
# print(s)
# print(s.index)


# s = pd.Series([10, 20, 30], index=[3,2,1])
# print(s)
# print(s.index)

# Task1:  print series indexes


# s = pd.Series([[1, 2, 3], [10, 20, 20]], index=["ind1", "ind2"])
# print(s)
# print(s.shape)


# s = pd.Series([[1, 2, 3], [10, 20, 20]], index=["ind1", "ind2"])
# s = pd.Series([10, 20, 230, 10.1, "hello"])
# print(s)
# print(s.dtype)


# s = pd.Series([10, 20, 230, 10, 60, 70, "hdsdfsddfsdfe"])
# print(s)
# print(s.size)   # count no of elem means size of series


# s1 = pd.Series([10, 20, 230, 10, 60, 70, "hdsdfsddfsdfe"])
# s2 = pd.Series()
#
# print(s1.empty)
# print(s2.empty)


# s1 = pd.Series([10, 20, 230, 10, 60, np.nan, "hdsdfsddfsdfe"])
# s2 = pd.Series()
#
# print(s1.hasnans)
# print(s2.hasnans)



# s1 = pd.Series([10, 20, 230, 10, 60])
# s2 = pd.Series()
#
# print(s1.nbytes)
# print(s2.nbytes)


# s1 = pd.Series(["hi", "Hsdfki"])
# s2 = pd.Series()
#
# print(s1.nbytes)
# print(s2.nbytes)


# s1 = pd.Series([54.45, 66.56, 67.54])
# s2 = pd.Series()
#
# print(s1.nbytes)
# print(s2.nbytes)


# s1 = pd.Series([[1, 2, 3], [200, 30, 40]])
# s2 = pd.Series()
#
# print(s1.ndim)
# print(s2.ndim)


# s1 = pd.Series([[1, 2, 3], [200, 30, 40]])
# s2 = pd.Series()

# print(s1.size)
# print(s2.size)


# dic = {"marks": 20, "name": "Rose Baby"}
# s1 = pd.Series(dic)
# print(s1)