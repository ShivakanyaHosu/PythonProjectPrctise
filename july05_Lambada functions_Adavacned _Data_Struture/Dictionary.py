my_dict = {"name": "Aman",
           "age": 34,
           "role": "SDET",
           "Experience": 3}
print(my_dict)
print(my_dict["age"])

my_dict["role"] = "Automation Tester"  # update
print(my_dict)

del my_dict["Experience"]
print(my_dict)  # delete key

# Iterating
for key, value in my_dict.items():
    # print(key, value)
    print(key, "->", value)
print("age" in my_dict)
