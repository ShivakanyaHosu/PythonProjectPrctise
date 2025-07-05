list_of_unique_items = {1, 2, 3, 4, 5, 5, 4, 6}
print(list_of_unique_items)

list1 = [33.4, 22.1, 22, 77]
set1 = set(list1)  # converting list to set
print(set1)
tuple1 = (22, 44, 66, 88)
print(set(tuple1))  # converting tuple to set

set3 = set1.union(list_of_unique_items)  # all numbers will print
print(set3)
set4 = set1.intersection(list_of_unique_items)  # common part
print(set4)
set5 = set1.difference(list_of_unique_items)  # difference
set6 = list_of_unique_items.difference(set1)  # difference
print(set5, set6)
