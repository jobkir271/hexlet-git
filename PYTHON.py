#хочу выводить текст задом наперед c пробелом, если он равен 5 символам или 
#хочу выводить текст если там есть буква Л И более 4 символов не учитвая регистр без пробела,
#в ином случае выводить "НЕТУ"

# 1 ВЕРСИЯ
# def task(text:str) -> str:
#     result = ""
#     x = ""
#     c = 0
#     while c != 1 :
#         if len(text) == 5:
#             x = text[::-1]
#             result = x[0] + " " + x[1] + " "  + x[2] + " "  + x[3] + " "  + x[4] 
#             c += 1
            
#         elif len(text) >= 4 and 'л' in text.lower():
#             result = text 
#             c += 1 
#         else:
#             c += 1
#             result = "НЕТУ"
#     return  result

# print(task('кирилл'))


#2 убрал не нужный while, добавил .join() добавил ввод
def task(text:str) -> str:
    result = ""
    x = ""
    if len(text) == 5:
        result = " ".join(text[::-1]) 
        return "В слове ровно 5 символов! Задом наперед: " + result 
    elif len(text) >= 4 and 'л' in text.lower():
        result = text 
        return f"В слове {result}, {len(text)} символов и есть буква 'л' "
    else:
        return "В слове нет буквы 'л' и оно не из 5 символов"

user_word = input('Напиши слово и скажу тебе о нем кое-что: ')
print(task(user_word))





