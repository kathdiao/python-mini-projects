class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def bark(self):
        return f"{self.name} says Woof!"


    def food(self, food):
        return f"{self.name} is eating {food}!"


    def activities(self):
        return f"{self.name} is running!"



dog = Dog("Babi", 9)
print(f"My dog's name is {dog.name} and he's {dog.age} years old.")
print(dog.bark())
print(dog.food("chicken"))
print(dog.activities())

dog2 = Dog("kiwi", 2)
print(f"My second dog's name is {dog2.name} and he's {dog2.age} years old.")
print(dog2.bark())