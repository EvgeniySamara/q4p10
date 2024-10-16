# Задача 2. Совместное проживание
# Чтобы понять, стоит ли ему жить с кем-то или лучше остаться в гордом
# одиночестве, Артём решил провести необычное исследование. Для этого он
# реализовал модель человека и модель дома.
# Человек может (должны быть такие методы):
# ● есть (+ сытость, − еда);
# ● работать (− сытость, + деньги);
# ● играть (− сытость);
# ● ходить в магазин за едой (+ еда, − деньги);
# ● прожить один день (выбирает одно действие согласно описанному ниже
# приоритету и выполняет его).
# У человека есть (должны быть такие атрибуты):
# ● имя,
# ● степень сытости (изначально 50),
# ● дом.
# В доме есть:
# ● холодильник с едой (изначально 50 еды),
# ● тумбочка с деньгами (изначально 0 денег).
# Если сытость человека становится меньше нуля, человек умирает.
# Логика действий человека определяется следующим образом:
# 1. Генерируется число кубика от 1 до 6.
# 2. Если сытость < 20, то нужно поесть.
# 3. Иначе, если еды в доме < 10, то сходить в магазин.
# 4. Иначе, если денег в доме < 50, то работать.
# 5. Иначе, если кубик равен 1, то работать.
# 6. Иначе, если кубик равен 2, то поесть.
# 7. Иначе играть.
# По такой логике эксперимента человеку надо прожить 365 дней.
# Реализуйте такую программу и создайте двух людей, живущих в одном доме.
# Проверьте работу программы несколько раз.
# Подсказка № 1
# Используйте функцию random.randint(1, 6) для моделирования броска кубика. Это
# поможет определить случайное действие, которое будет выполнять человек в течение
# дня.
# Подсказка № 2
# Определите методы для каждого действия человека (например, eat, work, play,
# shop_for_food), чтобы каждый метод изменял соответствующие атрибуты человека
# и дома (сытость, еда, деньги).
# Подсказка № 3
# Создайте класс House, в котором будут храниться ресурсы (еда и деньги). Это поможет
# легко управлять ресурсами и отслеживать их изменения в течение времени.
# Подсказка № 4
# Проверьте, не достигла ли сытость человека нуля, в методе live_day. Если сытость
# упала ниже нуля, программа должна завершиться, чтобы указать на смерть
# персонажа.
# Подсказка № 5
# Используйте цикл для моделирования жизни человека в течение 365 дней. Этот цикл
# должен вызывать метод live_day каждый день и проверять, выжил ли человек.

class Human:
    '''
    Человек может (должны быть такие методы):
    ● есть (+ сытость, − еда);
    ● работать (− сытость, + деньги);
    ● играть (− сытость);
    ● ходить в магазин за едой (+ еда, − деньги);
    ● прожить один день (выбирает одно действие согласно описанному ниже
    приоритету и выполняет его).
    У человека есть (должны быть такие атрибуты):
    ● имя,
    ● степень сытости (изначально 50),
    '''
    def __init__(self,name,home):
        self.name = name
        self.hung_level = 50
        self.home = home

    def __str__(self):
        return f'{self.name=} {self.hung_level=} {self.home.__str__()}'

class Home:
    '''
    # В доме есть:
    # ● холодильник с едой (изначально 50 еды),
    # ● тумбочка с деньгами (изначально 0 денег).
    '''
    __id = 0
    def __init__(self,refr=50,money=0):
        self.refr = refr
        self.money = money
        Home.__id+=1
        self.id = Home.__id
    def __str__(self):
        return f' Дом №{self.id}'

home1 = Home()
hum1 = Human('Иван',home1)

print (hum1)