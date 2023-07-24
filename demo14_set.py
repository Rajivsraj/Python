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



st = {35, 56, 67, 23}
# st.remove(156)
# st.remove(56)
x = st.discard(56)
print(x)