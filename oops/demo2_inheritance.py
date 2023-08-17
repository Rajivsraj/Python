"""
class Student:
    def __init__(self):
        self.name = "Rahul"
        self.age = 20;
        print("This is Student Constructor")

    def show(self):
        print("Hi")

class Faculty(Student):
    def __init__(self):
        print("Faculty constructor")

    def f_function(self):
        print("Faculty instance method")

obj = Faculty()
obj.f_function()
"""



"""
class Student:
    def __init__(self):
        self.name = "Rahul"
        self.age = 20;
        print("This is Student Constructor")

    def show(self):
        print("Hi")
        
class Faculty(Student):
    def __init__(self):
        super().__init__()
        print("Faculty constructor")

    def f_function(self):
        print("Faculty instance method")

obj = Faculty()
obj.f_function()"""


"""
class Student:
    def __init__(self, nm):
        self.name = nm
        self.age = 20
        print("Student Constructor")


class Faculty(Student):
    def __init__(self, q, n):
        super().__init__(n)
        self.quali = q
        print("Faculty Constructor")


obj = Faculty("B.TECH", "Mohan")
print(obj.quali)
print(obj.name)
"""



"""
# Multilevel Inheritance
class Student:
    def __init__(self):
        self.name = "Mohan"
        self.age = 20
        print("Student Constructor")


class Parents(Student):
    def ShowStuDetail(self):
        print(f"name: {self.name} age: {self.age}")

class Faculty(Parents):
    def f_name(self):
        self.fname = "Mr. Verma"
        return self.fname

obj = Faculty()
obj.ShowStuDetail()
print(obj.f_name())
"""



# Heirarchical Inheritance
"""
class Student:
    def __init__(self):
        self.name = "Mohan"
        print("Student cons")

class Faculty(Student):
    pass

class Principal(Student):
    pass

class Admin(Student):
    pass

obj = Admin()
f = Faculty()
print(f.name)"""




# Multiple Inheritance
"""
class Student:
    def __init__(self):
        self.name = "Mohan"
        print("Student cons")

class Faculty:
    def f_detail(self):
        print("This is faculty details")

class Principal:
    def p_details(self):
        print("This is principal details")

class Admin(Student, Faculty, Principal):
    pass

obj = Admin()
obj.p_details()
obj.f_detail()"""




"""
class Student:
    def __init__(self):
        self.name = "Mohan"
        print("Student cons")

class Faculty:
    def f_detail(self):
        print("This is faculty details")

class Principal(Faculty):
    def p_details(self):
        print("This is principal details")

class Admin(Student, Principal):
    pass

obj = Admin()
obj.p_details()
obj.f_detail()"""





"""
class Student:
    def __init__(self):
        super().__init__()
        self.name = "Mohan"
        print("Student cons")

class Faculty:
    def __init__(self):
        super().__init__()
        print("Faculty constructor")
    def f_detail(self):
        print("This is faculty details")

class Principal:
    def __init__(self):
        super().__init__()
        self.name = "VK Pawar"
        print("Principal constructor")
    def p_details(self):
        print("This is principal details")

class Admin(Student, Faculty, Principal):
    def __init__(self):
        super().__init__()
        print("Admin constructor")

obj = Admin()

# give dynamic name to principal class
"""

# Duct Typing
"""class Human:
    def speak(self):
        print("in Manner")

class Chitthi:
    def speak(self):
        print("No sense")

def same(obj):
    obj.speak()

h = Human()
c = Chitthi()
same(h)
same(c)
"""



# Strong Typing
"""
class Human:
    def speak(self):
        print("in Manner")

class Chitthi:
    def speak(self):
        print("Sense")

class Laptop:
    def features(self):
        print("I have Features")


def same(obj):
    if hasattr(obj, "speak"):
        obj.speak()
    else:
        print("this method is not found")

h = Human()
c = Chitthi()
l = Laptop
same(h)
same(c)
same(l)"""


# Method Overloading
"""
class Calculator:
    def plus(self, a, b):
        return a+b

    def plus(self, x, y, z):
        return x+y+z

calc = Calculator()
print(calc.plus(10, 20, 30))"""



# Method Overriding
"""
class Calculator:
    def plus(self, a, b):
        return a+b

class One(Calculator):
    def plus(self, x, y, z):
        return x+y+z

calc = One()
print(calc.plus(10, 20, 30))"""


from multipledispatch import dispatch

class Student:
    @dispatch(int, int)
    def plus(self, a, b):
        return a+b

obj = Student()
print(obj.plus(10, "h"))