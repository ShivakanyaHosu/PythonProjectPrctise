import math

check_even_odd = lambda num: "Even" if num % 2 == 0 else "Odd"
print(check_even_odd(18))

op2 = lambda: math.pow(int(input("Enter the num\n")), 2)
print(op2())
