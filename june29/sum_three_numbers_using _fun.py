# create pgm to sum of three numbers from the user i/p , if user doesn't enter any numbers use default as 100,200,300

num1 = int(input("enter the num1\n"))
num2 = int(input("enter the num2\n"))
num3 = int(input("enter the num3\n"))


def sum_three_numbers(n1=100, n2=200, n3=300):
    return n1 + n2 + n3


result1 = sum_three_numbers(num1, num2, num3)
print(result1)
result2 = sum_three_numbers()
print(result2)
