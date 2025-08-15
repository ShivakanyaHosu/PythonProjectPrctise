# Take a input and create a class

class Person:

    def __init__(self):
        print("it will be called autometically")
        self.name = input("enter the name \n")
        self.age = int(input("enter the age \n"))
        self.phone_number = int(input("enter the phone number \n"))
        self.occupation = input("enter the occupation \n")

    def name_of_functions_to_display(self):
        print(f"Name is {self.name}", f"Age is {self.age}", f"Phone Number is {self.phone_number}",
              f"Occupation is {self.occupation}")


Person1 = Person()
Person1.name_of_functions_to_display()
