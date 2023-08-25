class Crud:
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
                row = "\t".join([empid, name, age, phone, "\n"])
                f.writelines(row)

                ask = str(input("Do you want to Continue Y/N: ")).upper()
                if ask == "Y":
                    continue
                else:
                    return False

    def show_record(self):
        with open("data.txt", "r") as f:
            print(f.read())

obj = Crud()
# obj.add_data()
# obj.show_record()