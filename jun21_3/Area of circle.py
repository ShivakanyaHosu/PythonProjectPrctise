# write a program to calculate the area of the circle using its radius (area = π · r2)
import math

# input r -> float
# pi = 3.14
# power = pow or **

r = float(input("enter the radius\n"))

A = 3.14 * (pow(r, 3))
print(A)
print(math.pi)
# or
A1 = 3.14 * (r ** 3)
print(A1)

print(f"Area of the circle => {A1:.3f}")

area = math.pi * math.pow(r, 3)
print(area)
