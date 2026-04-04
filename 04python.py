# decorator
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print(f"Запустилась функция: {func.__name__}")
#         print(f"У неё аргументы: {args}, {kwargs}")
#         result = func(*args, **kwargs)
#         print(f"Функция {func.__name__} завершилась")
#         return result
#     return wrapper
#
# @decorator
# def task_test(*args):
#     x = iter(args)
#     print(next(x))
#     print(next(x))
#     return ''
# print(task_test('ddd','dsda','dsadasdfa'))

r = 0
stroka = 'кирилл'

def decorator (func):
    def wrapper(*args,**kwargs):
        print(f"Запустилась {func.__name__}, с аргументами {args,kwargs}")
        result = func(*args,**kwargs)
        print("The end.")
        return result
    return wrapper

@decorator
def task(xd):
    r = 0
    while r < len(stroka):
        if r < xd:
            r += 1
            print('r еще меньше двух')

        else:
            print('r уже больше двух')
            r += 1
    return ""

print(task(2))

dict = {'key' : 'dasdas'}
binar = '2012201'
print(int(binar, 3))
print(dict['key'])


class PC:
    def __init__(self,name, videocatra, ozu):
        self.name = name
        self.videocatra = videocatra
        self.ozu = ozu
        print(self.name)
        print(self.videocatra)
        print(self.ozu)

pc1 = PC('rakfeler', '5060 ti','16')

print(pc1.name)
class NEW_PC(PC):
    def text(self):
        return f"Привет {self.name}, твой возраст {self.age}."

#выше надо добить бы
# laa = lambda pc : pc + 1
# print(laa(0))
# lm = list(filter(lambda pc: pc.name != 'rakfeler' or pc.name == 'r,'rakfeler'))
# print(lm)
# и ниже пример
class PC:
    def __init__(self, name, videocard, ozu):
        self.name = name
        self.videocard = videocard
        self.ozu = ozu

# 1. Создаём список из нескольких объектов (ПК)
pc_list = [
    PC('rakfeler', '5060 ti', '16'),
    PC('CyberBeast', 'RTX 4070', '32'),
    PC('rakfeler', 'GTX 1650', '8'), # Еще один ПК с таким же именем
    PC('OfficePro', 'UHD Graphics', '16')
]

# 2. Используем filter для отбора
# Допустим, мы хотим найти все ПК, где имя НЕ равно 'rakfeler'
filtered_list = list(filter(lambda pc: pc.name != 'rakfeler', pc_list))

# 3. Выводим результат
print("Компьютеры с именем, отличным от 'rakfeler':")
for pc in filtered_list:
    print(f"- {pc.name} ({pc.videocard})")


#next итераторы

p = range(2,10)
pint = iter(p)
print(next(pint))
print(next(pint))
print(next(pint))
#наследовние тест
class fly:
    def flyer(self):
        print('лечу!')

class run:
    def runer(self):
        print('бегу!')

class duck(fly,run):
    def duck(self):
        print('кря!')

donald_duck = duck()

print(donald_duck.flyer())