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


n = np.array([10, 20, 30, 40])

s = pd.Series(n)

print(s)

for x in s:
    print(x)