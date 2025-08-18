class father:
    key = "2bhk"

    def car(self):
        print("Father has a car -> Alto")
        print(self.key)


class son(father):  # inheriting
    key2 = "3bhk"

    def suv(self):
        print("MG Hector, Black")
        print(self.key2)


father_ref = father()
father_ref.car()

son_ref = son()
son_ref.suv()
# child class accessing parent class with attributes and methods
son_ref.car()
print(son_ref.key)
