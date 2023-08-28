
class Crud:
    file = "data.txt"
    def __init__(self):
        print("* WELCOME TO EMP PORTAL *")
        print("===========================")

        print("1 Add New Employee Record")
        print("2 Show All Employee Records")
        print("3 Delete a Employee Record")
        print("4 Update a Employee Record")
        # print("5 Add New Employee")

    def add_data(self):
        with open("data.txt", "a") as f:
            while True:
                empid = input("Enter Your Employee id: ")
                name = input("Enter your Name: ")
                age = input("Enter your Age: ")
                phone = input("Enter your Phone: ")
                if self.is_record_already_exists(empid):
                    ask = str(input("Want to add another new record Y/N: "))
                    if ask.upper() == "Y":
                        print("ADDING NEW RECORD")
                        print("===================")
                        continue
                    else:
                        row = "\t".join([empid, name, age, phone, "\n"])
                        f.writelines(row)
                        return False
                else:
                    row = "\t".join([empid, name, age, phone, "\n"])
                    f.writelines(row)

                    ask = str(input("Want to add another new record Y/N: "))
                    if ask.upper() == "Y":
                        print("ADDING NEW RECORD")
                        print("===================")
                        continue
                    else:
                        return False

    def show_record(self):
        with open("data.txt", "r") as f:
            print(f.read())

    @classmethod
    def show_single_record(cls):
        emp_id = input("Enter emp id to show single record: ")
        with open(cls.file, "r") as f:
            for line in f.readlines():
                if emp_id in line:
                    print("Record found")
                    print(line)
                    return  line
                else:
                    print("Record not found")
                    break

    @classmethod
    def is_record_already_exists(cls, empid):
        with open(cls.file, "r") as f:
            # emp_id = input("Enter your Employee id: ")
            # data = f.readline()
            for line in f.readlines():
                if empid in line:
                    print("This record already exists please enter another record")
                    return True

    @classmethod
    def update_record(cls):
        emp_id = input("Enter emp id: ")



obj = Crud()
# obj.add_data()
# obj.show_record()
# obj.existing_record_prohibited()
obj.show_single_record()