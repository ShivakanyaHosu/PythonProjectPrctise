class Person:
    # Attribute - what you have, => Instance varible, Data Varible
    id = None
    phone_number = None
    age = None
    adress = None

    def __init__(self, id, phone_number, age, adress):
        print("it will be called automatically")
        self.age = age
        self.id = id
        self.phone_number = phone_number
        self.adress = adress

    # Behaviour - what you can do
    def talk(self):
        print("I can talk")

    def walk(self):
        print("I can walk")

    def Sleep(self):
        print("I can sleep --> " + self.adress)

    def eat(self):
        pass


# Create an object of the class

# Sivakanya = Person() # Person() = Object, Sivakanya = Object reference
Sivakanya = Person(123, 9148760058, 26, "Shirol")
Asha = Person(234, 12344, 34, "hpsur")
Sivakanya.age = 11
Sivakanya.adress = "Shirol1"
Sivakanya.walk()
Sivakanya.Sleep()
Asha.Sleep()
print(Sivakanya.adress)
# Asha = Person()
# Pappu = Person() # we can create unlimited number of objects

Person(12, 44, 5, "s")  # object without reference
