pb_global = 21


def my_function():
    pb_local = 10
    print(pb_local)  # Local variable within the function
    print(pb_global)  # Global variable outside the function => public variable


my_function()
print(pb_global)
# print(pb_local) => we can't print local variable outside the function
