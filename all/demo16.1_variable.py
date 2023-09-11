x = 20

def total():
    return 100

d = globals()
# print(d["total"])
# print(d["x"])
# print(globals())

print(d["total"]())
