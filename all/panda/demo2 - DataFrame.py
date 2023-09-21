import pandas as pd

# CREATE DataFrame using DICTIONARY
# ============================================

# DataFrame with single column
# dic = {
#     "rollno": [101, 102, 103, 104]
# }
#
# df = pd.DataFrame(dic)
# print(df)


# DataFrame with multiple column
# dic = {
#     "rollno": [101, 102, 103, 104],
#     "name": ["Rahul", "Sumti", "Amit", "Ajay"],
#     "maths": [50, 64, 75, 75],
#     "english": [40, 78, 85, 84]
# }
#
# df = pd.DataFrame(dic)
# print(df)


#2  CREATE DataFrame using LIST
# ============================================

# Data frame with Single column
# lst = [10, 20, 30, 40]
#
# df = pd.DataFrame(lst)
# print(df)


# lst = [[10, 20, 30], [40, 60, 80], [20, 30, 54]]\
# df = pd.DataFrame(lst)
# print(df)


#3 CREATE DataFrame using Numpy arrays
# ============================================

import numpy as np

# arr1 = np.array([10, 20, 30])
# arr2 = np.array([11, 21, 31])
#
# df = pd.DataFrame([arr1, arr2])
#
# print(df)



# arr1 = np.array([10, 20, 30])
# arr2 = np.array([11, 21, 31])
# arr3 = np.array([arr1, arr2])
# a = [20 20, 30]
# lst = [[20, 30, 40], [20, 20, 20]]
# df = pd.DataFrame(arr3)
#
# print(df)


#4 CREATE DataFrame using PANDAS SERIES

# sr = pd.Series([10, 20, 34, 30])
#
# df = pd.DataFrame(sr)
# print(df)



# sr1 = pd.Series([10, 20, 34, 30])
# sr2 = pd.Series([11, 12, 13 ,14])
#
# df = pd.DataFrame([sr1, sr2])
# print(df)


# sr1 = pd.Series([10, 20, 34, 30])
# sr2 = pd.Series([11, 12, 13, 14])
# sr4 = pd.Series([11, 12, 13, 14])
#
# sr3 = pd.Series([sr1, sr2])
# print(sr3)


# df = pd.DataFrame([sr1, sr2])
# df = pd.DataFrame(sr3)
# print(df)


#
# dic = {
#     "rollno": [101, 102, 103, 104],
#     "name": ["Rahul", "Sumit", "amit", "ajay"],
#     "city": ["New Delhi", "mumbai", "punjab", "Haryana"]
# }
#
# df = pd.DataFrame(dic)
# print(df["rollno"][2])

# print using loop



# add new col
# dic = {
#     "rollno": [101, 102, 103, 104],
#     "name": ["Rahul", "Sumit", "amit", "ajay"],
#     "city": ["New Delhi", "mumbai", "punjab", "Haryana"],
#     "marks": [546, 75 ,67, 67]
# }
#
# df = pd.DataFrame(dic)
#
# df["extramarks"] = df["marks"]+10
#
# print(df)



# dic = {
#     "sem1": [101, 102, 103, 104],
#     "sem2": [10, 20, 30, 40]
# }
#
# df = pd.DataFrame(dic)
#
# df["final"] = df["sem1"] + df["sem2"]
#
# print(df)


dic = {
    "rollno": [101, 102, 103, 104],
    "name": ["Rahul", "Sumit", "amit", "ajay"],
    "city": ["New Delhi", "mumbai", "punjab", "Haryana"],
    "marks": [546, 75 ,67, 67]
}

df = pd.DataFrame(dic)
print(df)

# del df["marks"]
# print(df)

df.pop("city")

print(df)


# loop
#     - series
#     - df
#
# slicing
#     - series
#     - df