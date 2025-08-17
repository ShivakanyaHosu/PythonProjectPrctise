class car:

    def __init__(self):
        self.password = 'shivakanya'  # public instance variable
        self.__secure_password = 'shiva'  # private instance varible

    def changepassword(self):
        print(self.password)
        # print(self.__secure_password)
        # we can change the password
        self.__secure_password = "123"
        print(self.__secure_password)


car1 = car()
print(car1.password)
# print(car1.__secure_password)
print(car1.changepassword())
