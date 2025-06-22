import keyword

print(keyword.kwlist)

age = 78  # int
print(age)
pi = 3.142  # float
name = "shivakanya"  # string(str)

age = age + 1
print(age)

isMale = True
print(type(isMale))

# Python is dynamically typed
AGE = 34
age = 35
print(AGE)
print(age)
print(type(AGE))
print(type(age))
age = "shivakanya"
print(type(age))  # At the run time data of the variable can be changed

a, b, c = 12, 13, 45
print(a, b, c)
print("Asha", "Shivakanya")

# 34, 36 => 36
result = max(34, 36)
result_min = min(34, 36)
print(result, result_min)
