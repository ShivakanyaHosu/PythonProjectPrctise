class Calc1:
    def __init__self(self, a, b):
        print("DC")
        self.a = a
        self.b = b

    def Sum(self):
        return self.a + self.b

    def Sub(self):
        return self.a - self.b

    def Mul(self):
        return self.a * self.b

    def Div(self):
        return self.a / self.b


Ob_ref = Calc1(1, 2)
output = Ob_ref.Sub()
print(output)
