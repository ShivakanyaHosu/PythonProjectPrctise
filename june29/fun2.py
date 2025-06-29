# The can't return parameters
# 1. No return type, No parameters/Argument - NRNP no return keyword
def greet():
    print("hello")


greet()


# 2. No Return Type with Argument
def greet1(name):
    print(f"hello, {name}")


name = "shiva"
# name = input("enter the name\n")
greet1(name)


# 3. No Return Type default argument (# Positional Argument)
def default_argument(name="Shiva"):
    print(name.upper())


default_argument("Kanya")
default_argument()


# Multi[ple Arguments
def multiple_arguments(name1="A", name2="B"):
    print("multiple arguments", name1, name2)


multiple_arguments()
multiple_arguments("lucky")  # default it will take name1
multiple_arguments("shiva", "kanya")
multiple_arguments(name1="Shiva")
multiple_arguments(name1="shiva", name2="kanya")


# 4. Argument + Return Type
def sum_of_two_numbers(a, b):
    return a + b


result = sum_of_two_numbers(a=4, b=5)
print(result)
result = sum_of_two_numbers(4, 5)
print(result)


# with default
def sum_of_two_numbers_default(num1=38, num2=45):
    return num1 + num2


print(sum_of_two_numbers_default(45, 78))
print(sum_of_two_numbers_default())
