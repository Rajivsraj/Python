from abc import ABC, abstractmethod


class Crud(ABC):
    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def update(self):
        pass

    def show(self):
        print("I'm concreate method")

# can't create object of abstract class
# obj = Crud()

class Student(Crud):
    def create(self):
        print("this is create method")

    def update(self):
        print("This is Update method")


stu = Student()
stu.show()
stu.create()