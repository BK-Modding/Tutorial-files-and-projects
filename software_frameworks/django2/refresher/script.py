# variables, data types and print statements:

age = 16
name = "BK"
# print("Hello my name is {} and I'm {} years old".format(name, age))
todayIsCold = False
# if and comments:
#
# if age > 18:
#     print("can go on ride")
# else:
#     print("can NOT go on ride")

# functions:

# def hello(thestring, age):
#     return "Hello {}, you are {} years old".format(thestring, age)
#
# print(hello(name, age))

# lists:

# dog_names = ["Fido", "Sean", "Sally", "Mark"]
# print(dog_names)
#
# del dog_names[2]
# print(len(dog_names))

# loops:

# you know it

# dictionaries:

# dogs = {"Fido": 8, "Sally": 17, "Sean": 2}
# print(dogs["Sean"])
#
# del dogs["Sean"]
# print(dogs)
#
# dogs["Sarah"] = 6
# print(dogs)

# classes:

class Dog:

    dog_info = "Hey dogs are cool"

    def __init__(self, name):
        self.name = name
    def bark(self):
        print("{} is barking".format(self.name))

noomi = Dog("My dog")
noomi.bark()
noomi.kappa = 5
print(noomi.kappa)

print(Dog.dog_info)