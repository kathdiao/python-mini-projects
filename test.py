
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def talk(self):
        print(f"Hi, my name is {self.name} I am {self.age} years old")

kath = Person("Katherine",22)
kath.talk()