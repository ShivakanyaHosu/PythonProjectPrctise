class Grandfather:
    gold = "2kg"

    def bhk1(self):
        print("1bhk")


class father(Grandfather):
    diamond = "2kg"

    def bhk12(self):
        print("2bhk")


class son(father):
    btc = "2kg"

    def bhk3(self):
        print("3bhk")


son_ref = son()
son_ref.bhk12()
son_ref.bhk1()
print(son_ref.gold)
print(son_ref.diamond)

print("-------")
father_ref = father()
father_ref.bhk1()
print(father_ref.gold)
