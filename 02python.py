#потестим новые штуки и сделаю новое придуманное задание
# threading +
# lambda Filter, map +
#  pass, contineum , branch +
# *args **kwargs +
# dict, list, tuple
# дандер +

import threading



# дандер магический метод и ссылки self
class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def text (self):
        return f"Привет {self.name}, твой возраст {self.age}."

Kirill = Player("Kirill", 23)
Player2 = Player("ILUSHA", 20)

print(Kirill.text())

# *args **kwargrs

def list_productov(*args):
    args_list = ", ".join(args)
    result = f'Продукты: {args_list}'
    return result

def list_kwargs(**kwargs):
    kwargs_list = ", ".join(f'{key}: {value}' for key, value in kwargs.items())
    result = f'Продкуты и их название: {kwargs_list}'
    return result

print(list_productov('apple','bananas'))
print(list_kwargs(product1 = 'apple', product2 = 'bananas'))

# lambda filter,map

labda_f = lambda x: x + 2
print(labda_f(2))

lambda_filter = list(filter(lambda x: x == 'o', 'moloko'))
print(lambda_filter)

lambda_map = list(map(lambda x: x * 2, range(10)))
print(lambda_map)


t1 = threading.Thread(target = list_productov, args = ('apple', 'bananas'))
t2 = threading.Thread(target = list_kwargs, kwargs = {'product1': 'apple','product2' : "bananas"})


t1.start()
t2.start()

t1.join()
t2.join()

#pass

def kirillUstal (text):
    i = 0
    x = 0
    while True:

        if text == "Kirill":
            pass
        elif text == "ILUSHA":
            x += 1
            continue
        else:
            x = "noneee"
            break
    return i, x
print(kirillUstal("IddLUSHA"))


#dict

name_use = {'product1' : 'apple', 'product2' : 'bananas'}
print(", ".join(name_use))
list1 = ('dsada', 'dasda')