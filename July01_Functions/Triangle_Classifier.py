def classify_triangle(a, b, c):
    if a > 0 and b > 0 and c > 0:
        if a + b > c and b + c > a and c + b > a:
            if a == b == c:
                return "Equilateral"
            elif a == b or b == c or c == a:
                return "Isosceles"
            else:
                return "Scalene"
        else:
            print("Not a Triangle")
    else:
        print("Not valid length")


side1 = float(input("enter the first side: "))
side2 = float(input("enter the second side: "))
side3 = float(input("enter the third side: "))

result = classify_triangle(side1, side2, side3)
print(f"Triable is classified as: {result}")
