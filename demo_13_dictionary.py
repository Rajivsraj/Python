"""
dic = {
    "name": "Rahul",
    "age": 19,
    "class": "7th",
    "dob": "20-dec-2003"
}
print(dic)
"""
"""
dic = ({
    "name": "Rahul",
    "age": 19,
    "class": "7th",
    "dob": "20-dec-2003"

})

print(dic)"""
"""
dic = ({
    "age": 19,
    "class": "7th",
    "name": "Rahul",
    "dob": "20-dec-2003"
})

print(dic["name"])
del dic["name"]
dic["name"] = "Mohan"
print(dic["name"])
print(dic["age"])
"""

"""
dic = ({
    "age": 19,
    "class": "7th",
    "name": "Rahul",
    "dob": "20-dec-2003"
})


for key in dic:
    print(key, end=" ")
"""




"""dic = ({
    "age": 19,
    "class": "7th",
    "name": "Rahul",
    "dob": "20-dec-2003"
})

print(dic)
dic.clear()
print(type(dic))"""



"""dic = ({
    "age": 19,
    "class": "7th",
    "name": "Rahul",
    "dob": "20-dec-2003"
})

dic2 = dic
print(dic)
print(dic2)


dic2["name"] = "raman"
print(dic)
print(dic2)"""


# dic = ({
#     "age": 19,
#     "class": "7th",
#     "name": "Rahul",
#     "dob": "20-dec-2003"
# })
#
# dic2 = dic.copy()
# print(dic)
# print(dic2)
#
# dic2["name"] = "raman"
# print(dic)
# print(dic2)



"""
dic = ({
    "age": 19,
    "class": "7th",
    "name": "Rahul",
    "dob": "20-dec-2003"
})

y = {}
x = y.fromkeys("name", "Sohan")
print(x)
print(y)
"""

""""
dic = ({
    "age": 19,
    "class": "7th",
    "name": "Rahul",
    "dob": "20-dec-2003"
})"""

# print(dic["name"])
# print(dic.get("name"))
# print(dic.items())

"""for x in dic.items():
    print(x)
"""

"""for x in dic.keys():
    print(x)
"""



"""for x in dic.values():
    print(x)"""
# dic.pop("name")

# dic.popitem()
# print(dic)


dic = {
    "name": "Rahul",
    "age": 19,
    "class": "7th",
    "dob": "20-dec-2003"
}

# x = dic.popitem()
# print(x)

# x = dic.setdefault("dept","sales")
x = dic.update({"dept": "sales"})
print(x)
print(dic)