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


"""
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
"""

"""
# Class Variable
class Company:
    name = "RSUniverse Computer Institute"  #class variable

    def __init__(self):
        self.city = "New Delhi" #instance Variable
        self.country = "India"  #instance Variable

    def access_instance_var(self):
        print(self.city)    # access instance variable
        print(self.name)    # access cls variable

cmp1 = Company()
print(cmp1.city)
print(cmp1.name)
cmp1.access_instance_var()


cmp2 = Company()
cmp2.name = "Hello Company"
print(cmp2.name)"""


"""
# object only get attributes and instance methods copy not values
class Company:
    cmp_name = "RSUniverse Computer Institute"

    def set_val(self, ag, c):
        self.age = ag
        self.city = c


obj1 = Company()
obj1.set_val(20, "delhi")
print(obj1.cmp_name)
print(obj1.age)

obj2 = Company()
print(obj2.age)
"""

"""
# class variable
class Mobile:
    
    brand = "Samsung"   # class variable

    print("hello")  # wrong way to use
    # class method
    @classmethod
    def a_cls_var(xyz):
        print(xyz.brand)

    def ok(self):
        self.x = "hello"

obj1 = Mobile()
obj1.a_cls_var()
print(obj1.brand)
obj1.ok()
print(obj1.x)
"""


# access class variable outside the class
"""
class Mobile:
    brand = "Samsung"  # class variable

    # class method
    @classmethod
    def a_cls_var(xyz):
        print(xyz.brand)

obj1 = Mobile()
# print(Mobile.brand)
# print(obj1.brand)

# obj1.brand = "New Brand" # overriding class value using object
# print(obj1.brand)

# obj2 = Mobile()
# print(obj2.brand)

Mobile.brand = "New Brand"
print(obj1.brand)

obj2 = Mobile()
print(obj2.brand)"""


# Static Method
class Mobile:
    @staticmethod
    def static_method(a, b):
        one = a
        two = b
        print(one+two)

nokia = Mobile()
nokia.static_method(10, 20)
print(nokia.one)