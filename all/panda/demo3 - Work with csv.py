import pandas as pd
# stu_details = {
#     "rollno": [101, 102, 103, 104],
#     "name": ["Rahul", "Shristi", "Asmit", "Neetu"],
#     "city": ["Delhi", "Mumbai", "Punjab", "Haryana"],
#     "salary": [10000, 20000, 49056, 56546]
# }

# print(stu_details)
# print(stu_details["rollno"])

# df = pd.DataFrame(stu_details)

# print(df) # will return whole data in table format

# Return only roll no values
# print(df["rollno"])
# print(df["name"])


# Insert DataFrame data into CSV File
# stu_details = {
#     "rollno": [101, 102, 103, 104],
#     "name": ["Rahul", "Shristi", "Asmit", "Neetu"],
#     "city": ["Delhi", "Mumbai", "Punjab", "Haryana"],
#     "salary": [10000, 20000, 49056, 56546]
# }
#
# # df = pd.DataFrame(stu_details)
# # csv = comman seperated value
# # excel = binary format
#
# df = pd.DataFrame(stu_details)
# df.to_csv("csv/file1.csv", index=False)
# df["age"] = [10, 20, 30, 40]
# df.to_csv("csv/file1.csv", index=False)


# # Read Data from CSV FILE
# df = pd.read_csv("csv/emp_details.csv")
# print(df.to_string(index=False))

  
# df = pd.read_csv("csv/emp_details.csv")
# print(df)


# dic = {
#     "name": pd.Series([1, 2, 3, 4], index=["a", "b", "c", "d"]),
#     "marks": pd.Series([30, 40, 50, 50, 60], index=["aa", "bb", "cc", "dd", "ee"])
# }
#
# df = pd.DataFrame(dic)
# print(df)


df = pd.read_csv("csv/emp_details.csv")
# print(df)
# print(df["name"])

# print(df.loc[0])
# print(df.loc[0:5])

# print(df.loc[0:5, ["name", "city"]])
# print(df.loc[5:8, ["name", "city"]])
# print(df.loc[:, ["name", "city"]])
# print(df.loc[:, ["name", "city"]])

# print(df)
# print(df.iloc[0, 3])
# print(df.iloc[0, 4])

# print(df.iloc[:3, 3])
# print(df.iloc[:3, 1:4])

# print(df.head())
# print(df.head(7))

# print(df.tail())
# print(df.tail(6))