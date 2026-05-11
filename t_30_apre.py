class Bird:

    wings = 2  # атрибут класса

    def __init__(self, name):
        self.name = name  # атрибут объекта

    # Обычный метод - работает с объектом
    @classmethod
    def get_name(cls):
        return cls.name

    # Классметод - работает с классом
    @property
    def get_wings(self):
        return self.wings  # cls = Bird

    name = 'fsdf'
# Использование
obj = Bird("Кеша")
print(Bird.get_name())  # "Кеша" - нужен объект
print(obj.get_wings)  # 2 - не нужен объект, просто класс

# propery = x.fly() -> x.fly из метода, аргумент
# сlassmethod = позволяет работать не с объектом, а с классом и берет аргументы класса
# staticmetod
