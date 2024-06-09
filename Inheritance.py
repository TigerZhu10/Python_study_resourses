
#* parent class:
class Animal:
    def __init__(self,name):
        self.name = name

#* child class_1(with init):
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print(f"{self.name} says skibidi toilet")
        
#* child class_2(without init)
class Cat(Animal):
    def speak(self):
        print(f"{self.name} says meow")

dog = Dog("Buddy")
my_cat = Cat("skibidi ohoi")

print(dog.name)
dog.speak()

print(my_cat.name)
my_cat.speak()

