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

  
df = pd.read_csv("csv/emp_details.csv")
print(df)