string = input("enter the string\n")
char_count = {}
for char in string:
    char_count[char] = char_count.get(char, 0) + 1
print(char_count)
