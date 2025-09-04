from logging import exception

print("start of the program")
try:
    a = int(input("enter the num1"))
    b = int(input("enter the num2"))

    c = a / b

    print(c)

except Exception as e:
    print(e)

print("end the program")
