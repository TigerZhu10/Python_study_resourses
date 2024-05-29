

class Dog: 
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #method(方式，方法)
    def bark(self):
        print(f"{self.name} says Woof!\n")
    



my_dog = Dog("Buddy", 3)
your_dog = Dog("Annie", 5)

print(your_dog.name)
print(your_dog.age)

your_dog.bark()

print(my_dog.name)
print(my_dog.age)

my_dog.bark()

#Example:
class Car:
    def __init__(self):
        self.speed = 0

    def accelerate(self):
        self.speed +=5

    def brake(self):
        if self.speed >= 5:
            self.speed -= 5
        else:
            self.speed = 0

    def get_speed(self):
        return self.speed
    
my_car = Car()

print("Initial speed:", my_car.get_speed())

my_car.accelerate()
print("speed after acceleration:", my_car.get_speed())

my_car.brake()
print("speed after braking:", my_car.get_speed())



'''

#! def = initializer(初始化器)
#? name and age = Attributes(属性)
## my_dog = object

#note self 和 __init__一定要写  
def __init__(self, a, b):
    self.a = a
    self.b = b

    
'''