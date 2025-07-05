# print th number 1 to 100
# multiple of 3 print "Fizz"
# multiple of 5 print "Buzz"
# multiple of both "FizzBuzz"

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:  ## need to take last condition as first to avoid print fizz or buzz print first
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
