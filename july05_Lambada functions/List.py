my_list = [1, 2, 3, "shiva"]
print(my_list)
print(len(my_list))
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])

# we can reassign value
my_list[0] = "Ram"  # list is mutable
my_list[1] = "Seetha"

print(my_list)
# ---- we iterate using for loop
for item in my_list:
    print(item)

my_list.append(5)  # it will add at the end
print(my_list)
my_list.extend([7, 8, 9])
print(my_list)

my_list.insert(1, " Rani")
print(my_list)

my_list.remove("Seetha")
print(my_list)

my_list_copy = my_list.copy()
print(my_list)
print(my_list_copy)

my_list_1 = [4, 6, 2, 1]
print(my_list_1)
my_list_1.sort()
print(my_list_1)

my_list_1.pop()
print(my_list_1)
