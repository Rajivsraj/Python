"""class Mobile:
    def __init__(self, nm, ag):
        self.name = nm
        self.age = ag

    def ok(abc):
        print(abc.name)

samsung = Mobile("Rahul", 30)
# print(samsung.name)
# print(samsung.age)
samsung.ok()"""



"""class Mobile:
    def __init__(self, nm, ag):
        self.name = nm
        self.age = ag

    def sum(self):
        print(self.name)

    def sub(self):
        print("Subtract")

    def result(self):
        print("Result")


samsung = Mobile("Rahul", 30)
samsung.sum()"""

#
# class Mobile(object):
#
#     def __init__(self):
#         self.price = ""
#         self.brand = ""
#         self.color = ""
#
#     def setData(self, price, brand, color):
#         self.price = price
#         self.brand = brand
#         self.color = color
#
#     def showData(self):
#         print(f"Price: {self.price}, Brand: {self.brand} Color: {self.color}")
#
#
# nokia = Mobile()
# nokia.setData(70009, "Nokia", "Black")
# # print(nokia.price)
# nokia.showData()


#
# class Mobile(object):
#
#     def __init__(self):
#         self.price = ""
#         self.brand = ""
#         self.color = ""
#
#     def setData(self, price, brand, color):
#         self.price = price
#         self.brand = brand
#         self.color = color
#
#     def showData(self):
#         print(f"Price: {self.price}, Brand: {self.brand} Color: {self.color}")
#
#
# class Company(Mobile):
#     def companyDetails(self):
#         print("Company details")
#
#
# cmp = Company()
# cmp.setData(200, "Iphone", "Green")
# print(cmp.brand)


# Instance Variable
class Mobile(object):
    
    def __init__(self):
        self.price = "" #instance variable/ member variable / attribute
        self.brand = "" #instance variable
        self.color = "" #instance variable

    # instance Method/ member method
    def setData(self, price, brand, color):
        self.price = price
        self.brand = brand
        self.color = color

    def showData(self):
        print(f"Price: {self.price}, Brand: {self.brand} Color: {self.color}")


class Company(Mobile):
    def companyDetails(self):
        print("Company details")


cmp = Company()
x = Company()
cmp.setData(200, "Iphone", "Green")

x.setData(2000, "Ixphone", "xGreen")
print(x.price)