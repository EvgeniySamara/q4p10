# Задание 1. Отцы, матери и дети.
# Вася совсем заскучал на работе и решил побаловаться с кодом проекта. Он
# Реализуйте два класса: «Родитель» и «Ребёнок». У родителя есть:
# ● имя,
# ● возраст,
# ● список детей.
# И он может:
# ● сообщить информацию о себе,
# ● успокоить ребёнка,
# ● покормить ребёнка.
# У ребёнка есть:
# ● имя,
# ● возраст (должен быть меньше возраста родителя хотя бы на 16 лет),
# ● состояние спокойствия,
# ● состояние голода.
# Реализация состояний — на ваше усмотрение. Это может быть и простой «флаг»,
# и словарь состояний, и что-то поинтереснее.

class Parent:
    def __init__(self,name,age,childlist):
        self.name = name
        self.age = age
        self.childlist = childlist

    def to_String(self):
        return f'{self.name=},{self.age},{self.childlist}'

    def calm_child(self,child):
        child.steady = True
        print(f'{child.name} успокоился')

    def feed_child(self,child):
        child.feed(20)

class Child:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.hungry = 50
        self.steady = False
        self.maxfood =100

    def feed(self,food):
        if self.hungry+food<100:
            self.hungry = self.hungry+food
            print(f'{self.name} подкрепился')
        else:
            self.hungry = 100
            print(f'{self.name} сыт')




p1 = Parent('Иван',33,['Саша','Ника'])
ch1 = Child('Саша',3)
ch1 = Child('Саша',3)
print(p1.to_String())
p1.calm_child(ch1)
p1.feed_child(ch1)
p1.feed_child(ch1)
p1.feed_child(ch1)
