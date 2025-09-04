# multiple exceptions
print("start the program")
try:
    a = int(input("enter the num1"))
    b = int(input("enter the num2"))
    c = a / b


except ValueError as e:
    print(e)

except ZeroDivisionError as e:
    print(e)

else:
    print("result is ", c)

finally:
    print("This code is always executed")
