
#* parent class:
class Animal:
    def __init__(self,name):
        self.name = name

#* child class_1(with init):
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print(f"{self.name} says woof")
        
#* child class_2(without init)
class Cat(Animal):
    def speak(self):
        print(f"{self.name} says meow")

dog = Dog("Buddy")
my_cat = Cat("Jacky")

print(dog.name)
dog.speak()

print(my_cat.name)
my_cat.speak()

