def r(row):
    # for r in range(1, 5+1):
        for c in range(1, 5+1):
            if c == 1 or row == 1 or row == 3 or (row<=3 and c == 5) or row-c == 1:
                print("R ",end="")
            else:
                print("  ",end="")
        # print()


def a(row):
    for c in range(1, 5+1):
        if c == 1 or row == 1 or row == 3 or c == 5:
            print("A ",end="")
        else:
            print("  ",end="")

def h(row):
    for c in range(1, 5+1):
        if c == 1 or c == 5 or row == 3:
            print("H ",end="")
        else:
            print("  ",end="")

def u(row):
    for c in range(1, 5+1):
        if c == 1 or c == 5 or row == 5:
            print("U ",end="")
        else:
            print("  ",end="")


def l(row):
    for c in range(1, 5+1):
        if c == 1 or row == 5:
            print("L ",end="")
        else:
            print("  ",end="")


# def name(nm)
#     for x in nm:
#         if x  == "r"
#
#
def print_name(name):
    for row in range(1, 5+1):
        for char in name:
            if char == "r":
                r(row)
            elif char == "a":
                a(row)
            elif char == "h":
                h(row)
            elif char == "u":
                u(row)
            elif char == "l":
                l(row)
        print()

print_name("sumit")