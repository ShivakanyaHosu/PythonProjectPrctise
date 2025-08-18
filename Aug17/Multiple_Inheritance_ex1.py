class father:
    def father_money(self):
        return 5

    def home(self):
        print("father has home")


class mother:
    def mother_money(self):
        return 2

    def home(self):
        print("mother has home")


class son(father, mother):
    def son_info(self):
        print("son")


s = son()
print(s.son_info())
print(s.mother_money())
print(s.father_money())

print(s.home())  # it will call father class method
