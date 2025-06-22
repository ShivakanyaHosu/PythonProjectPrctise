name = "shivakanya"  # bunch of characters

# single quotes or double quotes both are string only
# no char type in the python

print(len(name))  # length always starts from the 1
print(name.upper())  # To convert upper case
print(name.lower())  # To conver lower case

age = "60"
age1 = 60
print(type(age))
print(type(age1))

print(type(int(age)))

# functions to convert => int(), float(), str(), bool()

# concatenation
print(name + str(1))

f_name = "Shivakanya"
l_name = "Hosur"
print(f_name + " " + l_name)

# \n is for adding new line
print("shivakanya\nhosur")
# \t is for adding 1 tab
print("shivakanya\thosur")

# \b is for 1 backspace ex: it will delete one character
print("shivakanya\bhosur")

# difference btw single and double character
# where this 'r' concept will use??

dir = r"C:\shivakanya\n.txt"
dir1 = r"C:\shivakanya\t.txt"
print(dir, dir1)
