"""
st = set()
print(type(st))
"""

"""st = set([34, 7, 567, 34, 67])
print(type(st))
"""

"""st = {35, 56, 67, 23}
print(type(st))
"""

"""st = {35, 56, 67, 23}
st[0] = 100
print(st)"""


"""st = {35, 56, 67, 23, 35, 23}
print(st)
"""


"""st = {35, True, 67, 23.5, 35, (3, 45, 34)}
print(st)
"""

# st = {35, 56, 67, 23, 35, 23}
# for x in st:
#     print(x)

"""st = {35, 56, 67, 23}
st.add(100)

print(st)"""


# st = {35, 56, 67, 23}
# st.update([100, 30])
# st.update(["hello"])
# st.update([2])
# st.update((2,))
# print(st)

# st = {35, 56, 67, 23}
# st.remove(156)
# st.remove(56)
# x = st.discard(56)
# print(x)


# st = {4, 45, 36, 25}
# print(st)
# print(st.clear())
# print(st)


# st = {4, 45, 36, 25}
# x = st.copy()
# print(st)
# print(x)
# st.discard(45)
# print(st)
# print(x)


# st = set()
# st.pop()
# print(st)

# st1 = {10, 20, 30, 60}
# st2 = {50, 60, 10, 20}

# 10, 20, 30, 60,50
# abc = st1.union(st2)
# print(abc)

# abc = st1.intersection(st2)
# print(abc)



# st1 = {10, 20, 30, 40, 60}
# st2 = {10, 20, 50, 60, 80}

# abc = st1.intersection_update(st2)
# print(st1)
# print(st2)


# st1 = {10, 20, 30, 40, 60}
# st2 = {10, 20, 50, 60, 80}

# abc = st1.difference(st2)
# print(abc)

# abc = st1.difference_update(st2)
# print(abc)
# print(st1)


st1 = {10, 20, 30, 40, 60, 80, 70, 100, 454,4,545,45, 1}
st2 = {10, 20, 30, 40, 60, 70, 80, 1}


# x = st1.issubset(st2)
x = st1.issuperset(st2)
print(x)