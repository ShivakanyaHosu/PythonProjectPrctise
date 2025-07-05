def add_extra_security(func):  # function as argument
    def wrapper():  # syntax
        print("1. Before the function is called")
        print("2.Add helmet, Dashcash, gloves, knee guards, License")
        func()
        print("3. After the function called")
        print("4. Secure driving leave all the items")

    return wrapper()


@add_extra_security
def driving_ola():
    print("ola")


@add_extra_security
def driving_scooty():
    print("Normal function")
    print("Driving scooty")
