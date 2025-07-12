# Dictionary from 2 lists

Keys = ["Name", "Age", "Address"]
Values = ["Shiva", 23, "Bagalkot"]
Values1 = ["Shiva", 23]

my_dict = dict(zip(Keys, Values))
my_dict1 = dict(zip(Keys, Values1))
print(my_dict)
print(my_dict1)

# Merge dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged_dictionary = dict1 | dict2
print(merged_dictionary)
print(merged_dictionary.get("d"))

# missing keys
dict3 = {'a': 1, 'b': 2, 'c': 3}
dict4 = {'a': 1, 'b': 2}
missing_keys = set(dict3.keys()) - set(dict4.keys())
print(missing_keys)
