message = "hello world"
print(message.title())
print(message.upper())
print(message.lower())

first_name = "Tiger"
Last_name = "Zhu"
full_name = first_name + " " + Last_name
print(full_name)
#This is how you write comment
'''
Comment 
'''
#operator 示例：
print(3+2)
print(3-2)
print(3*2)
print(3/2)#在c语言结果是1
print(4**2)#4的2次方
print(2*0.1)

age = 13
message = "Happy" + " " + str(age) + " " + "years old"
print(message)
#关于operator内容结束

#以下为List列表(array相似)
names = ["Alex", "Tiger", "Roger"]
print(names)
print(names[0])
names[0] = "AT"#修改ALEX[0]
print(names[0])

names.append("Jack")#增加Jack在最后的位置
print(names)

names.pop()#清除Jack(默认最后位置)
print(names)

names.sort()
print(names)

print(len(names))

#for loop示例：
for name in names :
    print(name)

for value in range(1,5):
    print(value)
print("-----------------")
for value in range(1,11,2):
    print(value)

#if 示例：
name = "Alex"
if name == "Tiger":
    print("I am Tiger")
else:
    print("I am not Tiger")

player = "Tracy"
if player not in names:
    print(player + " " + "is not in name list")

age = 12
if age < 4:
    print("age is below 4")
elif age < 18:
    print("age is below 18")
else:
    print("you know")

#dictionary 示例：
person = {'name': 'Alex', 'age': 30}
#起一个好名字，方便区分
print(person['name'])
print(person['age'])
#把person['age']删除掉然后打印全部内容，使用del:delete
del person['age']
print(person)

#good format:
people = {
    'name' : 'Alex',
    'age' : '13',
    'weight' : '180',
    'school' : 'Uvic'
}
for key in people.keys():
    print(key)
    
print(people.keys())
print(people.values()) 

#function 示例：
def greeting():
    print("Hello")

greeting()

def describe_pet(animal, name): 
    print("I have a " + animal + ", his name is " + name)
    

describe_pet('dog','Kevin')
describe_pet('kevin','dog')
describe_pet(name = 'kevin',animal = 'dog')

#class 示例：
#创建：
class Dog():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def sit(self):
        print(self.name + " is sitting")
    def roll_over(self):
        print(self.name + " rolled over")

#调用：
my_dog = Dog('Jack',6)

print("my dog's name is "+ my_dog.name)

my_dog.sit()
my_dog.roll_over()

#note for class:
'''
1. method = function
2. def __init__(self,name,age): self 必须写在第一位 
3. 必须先写完114 - 116行才写执行内容
4. 在function后面必须加上 self 例如 def sit(self)
5. self.name = name : self 的 name = name 
'''






