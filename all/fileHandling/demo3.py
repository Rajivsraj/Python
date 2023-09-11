# Pickling & Unpickling

import pickle
class Mobile:
    def __init__(self, price, name, camera):
        self.price = price
        self.name = name
        self.camera = camera

    def show_details(self):
        print(f"Mobile name is {self.name} and price is {self.price} camera is {self.camera} MP")

#
# # Serialize
# with open("student.dat", "wb") as f:
#     stu = Mobile(10000, "Samsung", "108")
#     stu2 = Mobile(85000, "Samsung2", "1080")
#     pickle.dump(stu, f)
#     pickle.dump(stu2, f)
#     print("Data Pickled")
#
# f = open("student.dat", "rb")
# print(f.read())
#
# with open("student.dat", "rb") as f:
#     stu_obj = pickle.load(f)
#     stu_obj2 = pickle.load(f)
#     stu_obj.show_details()
#     stu_obj2.show_details()
#
# # f = open("studata.txt", "w")
# #
# # stu_obj.show_details()
#
#



