# colors = ["синий",
#           "зелёный",
#           "красный"]
# a = input("Выберите цвет: ")
# if a in colors:
#     print("Вы угадали")
# else:
#     print("Вы не угадали")

# dus = ("1984", "О дивный новый мир", "451 градус по Фаренгейту")
# print("1984" in dus)

# fruit = {"Apple":
#          "red",
#          "Banan":
#          "yellow"}
# print(fruit)

# facts = dict()
# facts["код"] = "смешной"
# facts["Билл"] = "Гейтс"
# facts["основание"] = 1776
# print(facts["код"])
# print(facts["Билл"])
# print(facts["основание"])

# bill = dict({"Билл Гейтс": "Щедрый"})
# print("Билл Гейтс" in bill)

# books = {"Дракула": "Строкер",
#          "1984": "Оруэлл",
#          "Процесс": "Кафка"}
# del books["Процесс"]
# print(books)

# rhymes = {"1": "смех",
#           "2": "синий",
#           "3": "я",
#           "4": "этаж",
#           "5": "Жизниь"}
#
# n = input("Введите число: ")
# if n in rhymes:
#     rhyme = rhymes[n]
#     print(rhyme)
# else:
#     print("Не найдено")

# list_musician = ["MORGENSHTERN", "Miyagi & Эндшпиль", "Пошлая Молли", "madk1l"]
#
# list_coordinates = (52.643789, 42.829207, 55.718335, 37.795705, 55.694965, 37.678471)
#
# my_data = {"Height": "175",
#            "Weight": "60",
#            "Favorite color": "green",
#            "Favorite actor": "Billy Herington"
# }
# while True:
#     n = input("What do you want to know: ")
#     if n in my_data:
#         result = my_data[n]
#         print(result)

# dict_musician = {"MORGENSHTERN": "Пустой вокзал",
#                  "Miyagi & Эндшпиль": "Ночь",
#                  "Пошлая Молли": "#Habibati",
#                  "madk1l": "Martine Rose"
#
# }

# s = "What do you want to know?".upper()
# print(s)
# s = "WHAT DO YOU WANT TO KNOW?".lower()
# print(s)
# s = "word".capitalize()
# print(s)

# s = "Уильям {}".format("Фолкнер")
# print(s)

# last = "Фолконе"
# print("Уильям {}".format(last))

# autor = "Уильям Фолконе"
# year_born = "1897"
# print("{} родился в {}.".format(autor, year_born))

# n1 = input("Введите существительное: ")
# v = input("Введите глагол: ")
# abj = input("Введите прилагательное: ")
# n2 = input("Введите существительное: ")
#
# r = """Как обычно, {} {} {} {}
#     """.format(n1,
#                v,
#                abj,
#                n2)
# print(r)

# s = "Я прыгнул через голову.Это целых 2 метра".split(".")
# print(s)

# first_three = "абв"
# result = "+".join(first_three)
# print(result)

# s = "                                                   Москва".strip()
# print(s)

# try:
#     "Животное".index("а")
# except:
#     print("Ничего не найдено")

# print("Она сказала \"Непременно.\"")

# print("строка1\nстрока2\nстрока3")

# s = "Чехов"
# print(s[0])
# print(s[1])
# print(s[2])
# print(s[-2])
# print(s[-1])

# s_new_1 = input("Введите строку: ")
# s_new_2 = input("Введите вторую строку: ")
# s_old = "Вчера я написал {}. Вчера я ходил в {}".format(s_new_1, s_new_2)
# print(s_old)

# s = "олдос Хаксли родился в 1894 году"
# print(s.capitalize())

# s = "Где это? Кто это? Когда это?"
# print(s.split("?"))

# s = ["Рыжая", "Лиса", "перепрыгнула", "через", "низкий", "забор", "."]
# s_new = " ".join(s)
# s_new = s_new[0: -2] + "."
# print(s_new)

# s = "Ребенок - зеркало поступков родителей"
# s = s.replace("о", "0")
# print(s)

# s = "Хемингуэй".index("м")
# print(s)

# print("три" + "три" + "три")
# print("три" * 3)

# s = "И незачем так орать! Я и в первый раз прекрано слышал."
# print(s[:20])

# tv = ["Во все тяжкие", "Секретные материалы", "Фарго"]
# i = 0
# for show in tv:
#     new = tv[i]
#     new = new.upper()
#     tv[i] = new
#     i += 1
# print(tv)

# x = 10
# while x > 0:
#     print("{}".format(x))
#     x -= 1
# print("Happe New Year!!!")

# qs = ["What is your name?",
#       "Your best color?",
#       "What are you doing?"]
# n = 0
# while True:
#     print("Введи X для выхода: ")
#     a = input(qs[n])
#     if a == "X":
#         break
#     n = (n + 1) % 3

# for i in range(1, 6):
#     if i == 3:
#         continue
#     print(i)

# while input("д или н") != "н":
#     for i in range(1, 5):
#         print(i)

# s = ["Ходячие мертвецы", "Красавцы", "Клан Сопрано", "Дневник вампира"]
# for index, obj in enumerate(s):
#     print(index, obj)

# s = [1, 2, 3, 4, 5]
# for a in s:
#     i = input("Введите число: ")
#     if i == "X":
#         break
#     try:
#         i = int(i)
#     except ValueError:
#         print("Вы ввели не тот формат")
#     if i in s:
#         print("Вы угадали")
#     else:
#         print("Вы не угадали")

# list1 = [8, 19, 148, 4]
# list2 = [9, 1, 33, 83]
# list3 = []
# for i in list1:
#     for j in list2:
#         list3.append(i * j)
# print(list3)

# import random
# print(random.randint(1, 100))

# import statistics
# nums = [1, 5, 33, 12, 46, 33, 2]
# print(statistics.mean(nums))
# print(statistics.median(nums))
# print(statistics.mode(nums))

# class Ogange:
#     def __init__(self, w, c):
#         self.weight = w
#         self.color = c
#         self.mold = 0
#         print("создано!")
#
#     def rot(self, days, temp):
#         self.mold = days * temp
#
# orange = Ogange(6, "апельсин")
# print(orange.mold)
# orange.rot(10, 33)
# print(orange.mold)

# class Apple:
#     def __init__(self, w, c, s, t):
#         self.weight = w
#         self.color = c
#         self.size = s
#         self.taste = t

# import math as mt
# class Circle:
#     def __init__(self, r):
#         self.radius = r
#
#     def area(self):
#         return self.radius**2 * mt.pi
# circle = Circle(10)
# print(circle.area())

# class Triangle:
#     def __init__(self, c, f):
#         self.catet = c
#         self.footing = f
#
#     def area(self):
#         return 1/2 * self.catet * self.footing
# result = Triangle(4, 6)
# print(result.area())

# class Hexagon:
#     def __init__(self, f, s, t, fo, fi, si):
#         self.f = f
#         self.s = s
#         self.t = t
#         self.fo = fo
#         self.fi = fi
#         self.si = si
#
#     def calculate_perimeter(self):
#         return self.f + self.s + self.t + self.fo + self.fi + self.si
# result = Hexagon(1, 2, 3, 4, 5, 6)
# print(result.calculate_perimeter())

# class Data:
#     def __init__(self):
#         self.nums = [1, 2, 3, 4, 5]
#
#     def change_data(self, index, n):
#         self.nums[index] = n
#
# data_one = Data()
# data_one.nums[0] = 100
# print(data_one.nums)
#
# data_two = Data()
# data_two.change_data(0, 100)
# print(data_two.nums)
class PublicPrivateExample:
    def __init__(self):
        self.public = "безопасно"
        self._unsafe = "небезопасно"

    def public_method(self):
        pass

    def _unsafe_method(self):
        pass