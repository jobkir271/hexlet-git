#потестим новые штуки и сделаю новое придуманное задание
# threading
# lambda Filter, map
#  pass, counter , branch
# *args **kwargs
# dict, list, tuple
# дандер



class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def text (self):
        return f"Привет {self.name}, твой возраст {self.age}."

Kirill = Player("Kirill", 23)
Player2 = Player("ILUSHA", 20)

print(Kirill.text())
