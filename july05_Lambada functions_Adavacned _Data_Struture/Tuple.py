t = tuple()
print(t)

# convert tuple to list

tuple1 = tuple([1, 2, 3, 4])
print(tuple1)

tuple2 = ("rani", "raja")
newtuple = (tuple1, tuple2)
print(newtuple)  # two tuples

print(newtuple[0])  # first tuple will print => (1,2,3,4)
print(newtuple[0][0])  # 1
print(newtuple[1][1])  # raja

print("rani" in tuple2)
