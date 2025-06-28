num1 = int(input("enter the num1\n"))
num2 = int(input("enter the num2\n"))
num3 = int(input("enter the num3\n"))

if num1 > num2 and num1 > num3:
    print("Max is ", num1)
if num3 > num2 and num3 > num1:
    print("Max is ", num3)
else:
    print("Max is ", num2)
