from enum import nonmember


def first_non_repeating(string):
    for char in string:
        if string.count(char) == 1:
            return char
    return "none"


print(first_non_repeating("swiss"))
print(first_non_repeating("dada"))
