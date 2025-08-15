class Calc:
    def __init__self(self):
        print("DC")

    def Sum(self, a, b):
        return a + b

    def Sub(self, a, b):
        return a - b

    def Mul(self, a, b):
        return a * b

    def Div(self, a, b):
        return a / b


Object_ref = Calc()
a = float(input("enter the value of a \n"))
b = float(input("enter the value of b \n"))

out_sum = Object_ref.Sum(a, b)
out_sub = Object_ref.Sub(a, b)
out_mut = Object_ref.Mul(a, b)
out_div = Object_ref.Div(a, b)

print(out_div, out_sub, out_mut, out_sum)
