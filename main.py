# №1
from datetime import datetime
# class Book:
#     def __init__(self, name, create, izdat, year):
#         self.name = name
#         self.create = create
#         self.izdat = izdat
#         self.year = year
#         self.__genre = ''
#
#     def get_info(self):
#         print(f"Название: {self.name} \n"
#               f"Автор: {self.create} \n"
#               f"Издательство: {self.izdat} \n"
#               f"Год выпуска: {self.year} \n"
#               f"Жанр: {self.__genre}")
#     def old_book(self):
#         if self.year > datetime.now().year - 5:
#             print('Книга новая')
#         else:
#             print('Книга не новая')
#
#     @property
#     def genre(self):
#         return self.__genre
#
#     @genre.setter
#     def genre(self, value):
#         self.__genre = value
#
# book_1 = Book('гарри Потер', 'Джоан Роулинг', 'Прометей', 2026)
#
# book_1.genre = "Фентези"
#
# book_1.get_info()
# book_1.old_book()



# №2
# class Car:
#     def __init__(self, mark, model, year, after_to):
#         self.mark = mark
#         self.model = model
#         self.year = year
#         self.after_to = after_to
#         self.__type_topl = ''
#
#     def get_TO(self):
#         if self.after_to > 10_000:
#             print("Нужно ТО")
#         else:
#             print("ТО не нужно")
#
#     def get_info(self):
#         print(f"Марка машины: {self.mark} \n"
#               f"Модель машины: {self.model} \n"
#               f"Год выпуска: {self.year} \n"
#               f"Пробег: {self.after_to} \n"
#               f"Вид топлива: {self.__type_topl}")
#
#     @property
#     def type_top(self):
#         return self.__type_topl
#
#     @type_top.setter
#     def type_top(self, value):
#         self.__type_topl = value
#
# car_1 = Car('Dodge', 'Demon', 2017, 42_000)
#
# car_1.type_top = 'Дизель'
#
# car_1.get_info()
# car_1.get_TO()



# №3
# class Employee:
#     def __init__(self, surname,name, job_title, salary):
#         self.surname = surname
#         self.name = name
#         self.job_title = job_title
#         self.salary = salary
#         self.__job_experience = ""
#
#     def salary_statistic(self):
#         if self.salary > 100_000:
#             print("Зарплата сотрудника высокая")
#         else:
#             print("Зарплата сотрудника невысокая")
#
#     def get_info(self):
#         print(f"Фамилия: {self.surname} \n"
#               f"Имя: {self.name} \n"
#               f"Должность: {self.job_title} \n"
#               f"Зарплата: {self.salary} \n"
#               f"Опты работы: {self.__job_experience}")
#
#     @property
#     def job_experience(self):
#         return self.__job_experience
#
#     @job_experience.setter
#     def job_experience(self, value):
#         self.__job_experience = value
#
# people_1 = Employee("Нечаев", "Сергей", "военный", 200_000)
#
# people_1.job_experience = "5 лет"
#
# people_1.get_info()
# people_1.salary_statistic()



# №4
# class Product:
#     def __init__(self, name, prise, counted):
#         self.name = name
#         self.prise = prise
#         self.counted = counted
#         self.__category = ''
#
#     def check(self):
#         if self.counted > 0:
#             print("Товар есть в наличии")
#         else:
#             print("Товара нет в наличии")
#
#     def get_info(self):
#         print(f"Название товара: {self.name} \n"
#               f"Цена товара: {self.prise} \n"
#               f"Количество товара: {self.counted} \n"
#               f"Категория товара: {self.__category}")
#
#     @property
#     def category(self):
#         return  self.__category
#
#     @category.setter
#     def category(self, value):
#         self.__category = value
#
# product_1 = Product("Брилиант", 1_000_000, 2)
#
# product_1.category = "Драгоценные камни"
#
# product_1.get_info()
# product_1.check()



#№5
# from math import pi
# class Circle:
#     def __init__(self, rad):
#         self.rad = rad
#         self.__color = ''
#
#     def get_L(self):
#         print(f"Длина окружности: {pi * self.rad * 2}")
#
#     def get_S(self):
#         print(f"Площадь круга: {pi * self.rad**2}")
#
#     def get_info(self):
#         print(f"Радиус круга: {self.rad} \n"
#               f"Цвет круга: {self.__color}")
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.setter
#     def color(self, value):
#         self.__color = value
#
# circle_1 = Circle(10)
#
# circle_1.color = "Зелёный"
#
# circle_1.get_info()
# circle_1.get_L()
# circle_1.get_S()



#№6
# class Car:
#     def __init__(self, mark, model, year):
#         self.mark = mark
#         self.model = model
#         self.year = year
#
#     def check_age(self):
#         if self.year > 2015:
#             print("Машина относительно новая")
#         else:
#             print("Машина не новая")
#
#     def get_info(self):
#         print(f"Марка автомобиля: {self.mark} \n"
#               f"Модель: {self.model} \n"
#               f"Год выпуска: {self.year}")
#
#
# class Sedan(Car):
#     def __init__(self, mark, model, year, type_body):
#         super().__init__(mark, model, year)
#         self.type_body = type_body
#
#     def check_body(self):
#         if self.type_body == "Седан":
#             print("Это самый популярный тип кузова")
#         else:
#             print("Это не самый популярный, но практичный тип кузова")
#
#     def get_info(self):
#         super().get_info()
#         print(f"Тип кузова: {self.type_body}")
#
#
# class Truck(Car):
#     def __init__(self, mark, model, year, gruz):
#         super().__init__(mark, model, year)
#         self.gruz = gruz
#
#     def check_gruz(self):
#         if self.gruz > 23_000:
#             print("Грузовик способен перевести всё что угодно")
#         else:
#             print("Грузовик способен перевести многое, но не всё")
#
#
#     def get_info(self):
#         super().get_info()
#         print(f"Грузоподъёмность: {self.gruz}")
#
#
# class Bus(Car):
#     def __init__(self, mark, model, year, cnt_people):
#         super().__init__(mark, model, year)
#         self.cnt_people = cnt_people
#
#     def check_cnt_people(self):
#         if self.cnt_people > 60:
#             print("В автобусе много мест")
#         else:
#             print("Мест не так много")
#
#
#     def get_info(self):
#         super().get_info()
#         print(f"Количество мест: {self.cnt_people}")
#
#
#
# car_1 = Car("Dodge", "Demon", 2015)
# sedan_1 = Sedan("Mercedes", "E200", 2016, "Седан")
# truck_1 = Truck("Камаз", "400Т", 2011, 19_000)
# bus_1 = Bus("Электробус", "Eco", 2018, 70)
#
# cars = [car_1, sedan_1, truck_1, bus_1]
# for i in cars:
#     i.get_info()
#
#     if isinstance(i, Sedan):
#         i.check_body()
#     elif isinstance(i, Truck):
#         i.check_gruz()
#     elif isinstance(i, Bus):
#         i.check_cnt_people()
#     elif isinstance(i, Car):
#         i.check_age()
#     print()
#
#
# find_mark = input("Какую марку вы хотите найти: ")
# for car in cars:
#     if car.mark == find_mark:
#         car.get_info()
#
# find_age = int(input("Машину какого года выпуска вы хотите найти: "))
# for car in cars:
#     if car.year == find_age:
#         car.get_info()



#№7
# class Student:
#     def __init__(self, name, surname, age):
#         self.name = name
#         self.surname = surname
#         self.age = age
#
#     def check_age(self):
#         if self.age > 18:
#             print("Студенту стоит задуматься о военнике")
#         else:
#             print("Военкомат пока не заинтересован в студенте")
#
#
#     def get_info(self):
#         print(f"Имя студента: {self.name} \n"
#               f"Фамилия студента: {self.surname} \n"
#               f"Возраст студента: {self.age}")
#
#
# class Bac(Student):
#     def __init__(self, name, surname, age, curs):
#         super().__init__(name, surname, age)
#         self.curs = curs
#
#     def check_curs(self):
#         if self.curs > 3:
#             print("Студент скорее всего уже работает")
#         else:
#             print("Студент скорее всего  ещё не работает")
#
#     def get_info(self):
#         super().get_info()
#         print(f"Курс обучения: {self.curs}")
#
#
# class Mag(Student):
#     def __init__(self, name, surname, age, spec):
#         super().__init__(name, surname, age)
#         self.spec = spec
#
#     def check_spec(self):
#         if self.spec == "Програмист":
#             print("Студенту стетит работа в Биг-техе")
#         else:
#             print("Биг-тех пролетает")
#
#     def get_info(self):
#         super().get_info()
#         print(f"Специализация: {self.spec}")
#
#
# class Asp(Student):
#     def __init__(self, name, surname, age, topic):
#         super().__init__(name, surname, age)
#         self.topic = topic
#
#     def check_topic(self):
#         if self.topic == "Технологии ИИ":
#             print("Скорее всего работу написал объект его изучения")
#         else:
#             print("Он скачал работу с интернета")
#
#     def get_info(self):
#         super().get_info()
#         print(f"Тема диссертации: {self.topic}")
#
# stud_1 = Student("Олег", "Багратионов", 19)
# bac_1 = Bac("Кристина", "Дурова", 21, 3)
# mag_1 = Mag("Павел", "Германович", 22, "Програмист")
# asp_1 = Asp("Виктория", "Ланская", 25, "Технологии ИИ")
# students = [stud_1, bac_1, mag_1, asp_1]
# for i in students:
#     i.get_info()
#
#     if isinstance(i, Bac):
#         i.check_curs()
#     elif isinstance(i, Mag):
#         i.check_spec()
#     elif isinstance(i, Asp):
#         i.check_topic()
#     elif isinstance(i, Student):
#         i.check_age()
#     print()
#
# find_name = input("\nВведите имя искомого студента: ")
# for i in students:
#     if i.name == find_name:
#         i.get_info()
#
# find_age = int(input("\nВведите кур искомого студента: "))
# for i in students:
#     if isinstance(i, Bac):
#         if i.curs == find_age:
#             i.get_info()



#№8
# class Rest:
#     def __init__(self, name, address, type_kitchen):
#         self.name = name
#         self.address = address
#         self.type_kitchen = type_kitchen
#
#     def check(self):
#         if len(self.name) > 10:
#             print("Название заведения очень большое")
#         else:
#             print("Название будет не трудно запомнить")
#
#     def get_info(self):
#         print(f"Название заведения: {self.name} \n"
#               f"Адрес заведения: {self.address} \n"
#               f"Тип кухни: {self.type_kitchen}")
#
# class Italy(Rest):
#     def __init__(self, name, address, type_kitchen, rank):
#         super().__init__(name, address, type_kitchen)
#         self.rank = rank
#
#     def check_rank(self):
#         if self.rank < 4.7:
#             print("Может поискать другое место?")
#         else:
#             print("У места хорошие отзывы")
#
#
#     def get_info(self):
#         super().get_info()
#         print(f"Рейтинг заведения: {self.rank}")
#
#
# class Japan(Rest):
#     def __init__(self, name, address, type_kitchen,rank):
#         super().__init__(name, address, type_kitchen)
#         self.rank = rank
#
#     def check_Jap(self):
#         if "Вок" in self.name:
#             print("Это настоящий Японский ресторан")
#         else:
#             print("Может и не совсем Японский")
#
#
#     def get_info(self):
#         super().get_info()
#         print(f"Рейтинг заведения: {self.rank}")
#
#
# class Franc(Rest):
#     def __init__(self, name, address, type_kitchen,rank):
#         super().__init__(name, address, type_kitchen)
#         self.rank = rank
#
#     def check_Franc(self):
#         if self.type_kitchen != "Французский":
#             print("Как может быть рестроран французский, если там нет французской кухни")
#         else:
#             print("Мне кажется, что я нахожусь во Франции")
#
#
#     def get_info(self):
#         super().get_info()
#         print(f"Рейтинг заведения: {self.rank}")
#
# rest_1 = Rest("Теремок", "Улица строителей дом 6", "русская")
# rest_2 = Italy("Вайб Италии", "Речная 2", "Итальянская", 4.4)
# rest_3 = Japan("СушиВок", "Пушкинская 28", "японская",4.9)
# rest_4 = Franc("Клод Моне", "Невский проспект 44", "Французский", 5.0)
# rests = [rest_1, rest_2, rest_3, rest_4]
#
# for i in rests:
#     i.get_info()
#     if isinstance(i, Italy):
#         i.check_rank()
#     elif isinstance(i, Japan):
#         i.check_Jap()
#     elif isinstance(i, Franc):
#         i.check_Franc()
#     elif isinstance(i, Rest):
#         i.check()
#
#     print()
#
# find_kitchen = input("Введите тип кухни: ")
# for _ in rests:
#     if _.type_kitchen == find_kitchen:
#         _.get_info()
#
# find_rank = float(input("Ресторан с каким рейтпнгом вас интересует: "))
# for _ in rests:
#     if hasattr(_, "rank"):
#         if _.rank == find_rank:
#             _.get_info()



# №11
# class Shop:
#     def __init__(self, name):
#         self.name = name
#         self.list_shopping = []
#
#     def __len__(self):
#         return len(self.list_shopping)
#
#     def get_all_cost(self):
#         all_cost = 0
#
#         for i in self.list_shopping:
#             all_cost += i.cost * i.count
#
#         print(f"Общая стоимость товаров: {all_cost}")
#
# class Goods:
#     def __init__(self, name, cost, count):
#         self.name = name
#         self.cost = cost
#         self.count = count
#
#     def add_Shop(self, shop):
#        shop.list_shopping.append(self)
#
#     def remov_Shop(self, shop):
#         shop.list_shopping.remove(self)
#
#
# goods_1 = Goods("Яблоки", 100, 4)
#
# shop_1 = Shop("Магнит")
#
# goods_1.add_Shop(shop_1)
# print(len(shop_1))
# for i in shop_1.list_shopping:
#     print(i.name)
#
# shop_1.get_all_cost()



#№12
# class Task:
#     def __init__(self, name, description, stat):
#         self.name = name
#         self.description = description
#         self.stat = stat
#
#     def change_stat(self):
#         self.stat = "выполнено"
#
#     def __str__(self):
#         return f"Задача '{self.name}': {self.description}, статус - {self.stat}"
#
# task_1 = Task("Помочь маме", "помыть посуду", "не выполнено")
#
# print(task_1)
# task_1.change_stat()
# print(task_1)



#№13
# class Bank:
#     def __init__(self, name):
#         self.name = name
#         self.list_account = []
#
#     def __len__(self):
#         return len(self.list_account)
#
#     def all_balans(self):
#         all_money = 0
#         for i in self.list_account:
#             all_money += i.balans
#         return all_money
#
# class Account:
#     def __init__(self, numb, balans):
#         self.numb = numb
#         self.balans = balans
#
#     def add_account_in_bank(self, bank):
#         bank.list_account.append(self)
#
#     def remove_account_from_bank(self, bank):
#         bank.list_account.remove(self)
#
# acc_1 = Account(123, 1_000_000)
# acc_2 = Account(124, 1_000)
# bank_1 = Bank("Тинькофф")
# acc_1.add_account_in_bank(bank_1)
# acc_2.add_account_in_bank(bank_1)
# print(bank_1.all_balans())
# print(len(bank_1))
# for i in bank_1.list_account:
#     print(i.balans)



#№14
# class Student:
#     def __init__(self, name, surname, age, list_ocenk):
#         self.name = name
#         self.surname = surname
#         self.age = age
#         self.list_ocenk = list_ocenk
#
#     def add_oc(self, value):
#         self.list_ocenk.append(value)
#
#     def __len__(self):
#         return len(self.list_ocenk)
#
#     def get_sr_zn(self):
#         rez = sum(self.list_ocenk) / len(self.list_ocenk)
#         print(rez)
#
#     def get_info(self):
#         rez = sum(self.list_ocenk) / len(self.list_ocenk)
#         print(f"Студент {self.name} {self.surname}, возраст - {self.age}, средний балл - {rez}")
#
# st_1 = Student("Егор", "Елисеев", 19, [5, 5, 4])
# print(len(st_1))
# st_1.get_sr_zn()
# st_1.add_oc(5)
# st_1.get_sr_zn()
# st_1.get_info()



#№15
# class Car:
#     def __init__(self, mark, model, years_of_present, speed):
#         self.mark = mark
#         self.model = model
#         self.years_of_present = years_of_present
#         self.speed = speed
#
#     def increase_speed(self, value):
#         self.speed += value
#
#     def decrease_speed(self, value):
#         self.speed -= value
#
#     def __eq__(self, other):
#         return self.speed == other.speed
#
#
#     def get_info(self):
#         print(f"Автомобиль {self.mark} {self.model}, год выпуска - {self.years_of_present}, скорость - {self.speed}")
#
# car_1 = Car("Dodge", "Demon", 2017, 200)
# car_2 = Car("BMW", "E49", 1993, 170)
# car_3 = Car("Лада", "Веста", 2015, 150)
# car_1.get_info()
# car_1.increase_speed(10)
# car_1.get_info()
# print(car_1 == car_2)
# car_2.increase_speed(40)
# print(car_1 == car_2)
# car_3.decrease_speed(20)
# car_3.get_info()



# №16
# class Fruit:
#     def __init__(self, form, color, taste):
#         self.form = form
#         self.color = color
#         self.taste = taste
#         self.__weight = 0
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, value):
#         self.__weight = value
#
#     def get_weight(self):
#         print(f"Общий вес: {self.__weight}")
#
#     def __eq__(self, other):
#         return self.__weight == other.__weight
#
#
#     def get_info(self):
#         rez = "{:<13} | {:^10} | {:^10} | {:>7}"
#         print(rez.format("Форма", "Цвет", "Вкус", "Вес"))
#         print("-" * 50)
#         row = "{:<13} | {:^10} | {:^10} | {:>7}"
#         print(row.format(self.form, self.color, self.taste, self.__weight))
#
# fruit_1 = Fruit("Круглое", "Красное", "Сладкое")
# fruit_1.weight = 100
# fruit_1.get_info()
# fruit_2 = Fruit("Круглое", "Жёлтое", "Кислое")
# fruit_2.weight = 120
# print(fruit_1 == fruit_2)
# fruit_2.get_info()
# fruit_2.get_weight()



#№17
# class Calculate:
#     def add(self, a, b):
#         return a + b
#     def sum(self, a, b):
#         return a - b
#
# calc = Calculate()
# prim = input("Введите пример: ").split()
# rez = int(prim[0])
# i = 1
# while i < len(prim):
#     znak = prim[i]
#     num = int(prim[i + 1])
#
#     if znak == "+":
#         rez = calc.add(rez, num)
#     elif znak == "-":
#         rez = calc.sum(rez, num)
#
#     i += 2
# print("Результат:", rez)



#№18
# from math import pi
# class Circle:
#     def __init__(self, r):
#         self.r = r
#
#     def get_perimetr(self):
#         rez = 2 * pi * self.r
#         print(f"Периметр круга: {rez}")
#
# class Rectangle:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def get_perimetr(self):
#         rez = self.a * 2 + self.b * 2
#         print(f"Периметр прямоугольника: {rez}")
#
# circ_1 = Circle(4)
# rect_1 = Rectangle(6, 7)
# list_figure = [circ_1, rect_1]
# for i in list_figure:
#     i.get_perimetr()



#№19
# from datetime import datetime
#
# class House:
#     def __init__(self, etazh, cnt_pod, rayon, workers, srok_start, srok_end, collective):
#         self.etazh = etazh
#         self.cnt_pod = cnt_pod
#         self.rayon = rayon
#         self.workers = workers
#         self.srok_start = datetime.strptime(srok_start, "%d.%m.%Y")
#         self.srok_end = datetime.strptime(srok_end, "%d.%m.%Y")
#         self.collective = collective
#
#
# class Workers:
#     def __init__(self, name_company, cvalific):
#         self.name_company = name_company
#         self.cvalific = cvalific
#
#
# workers_1 = Workers("Пик", "плиточник")
# workers_2 = Workers("Пик", "монтажник")
#
# house_1 = House(20, 5, "Одинцово", [workers_1, workers_2], "21.01.2027", "21.12.2027", "бригада 1")
# house_2 = House(40, 7, "Таганка", [workers_2], "04.05.2027", "10.11.2027", "бригада 2")
#
# houses = [house_1, house_2]
#
#
# def check(worker, houses, year):
#     cnt = 0
#
#     for house in houses:
#         if worker in house.workers:
#             if house.srok_start.year <= year <= house.srok_end.year:
#                 cnt += 1
#     return cnt
#
# print(check(workers_2, houses, 2027))




#№20
# class Personal:
#     def __init__(self,name, salary, age_work):
#         self.name = name
#         self.salary = salary
#         self.age_work = age_work
#
#     def get_info(self):
#         print(f"Имя сотрудника: {self.name}\n"
#               f"Зарплата сотрудника: {self.salary}\n"
#               f"Стаж сотрудника: {self.age_work}")
#
# class Cass(Personal):
#     def __init__(self, name, salary, age_work):
#         super().__init__(name, salary, age_work)
#
#     def get_info(self):
#         super().get_info()
#
# class Merch(Personal):
#     def __init__(self, name, salary, age_work):
#         super().__init__(name, salary, age_work)
#
#     def get_info(self):
#         super().get_info()
#
# pers_1 = Personal("Ольга", 150_000, 6)
# cass_1 = Cass("Женя", 100_000, 3)
# merch = Merch("Кира", 160_000, 4)
# merch.get_info()



#№21
# class Rectangle:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def get_S(self):
#         print(f"Площадь прямоугольника: {self.a * self.b}")
#
#     def get_P(self):
#         print(f"Периметр прямоугольника: {(self.a + self.b) * 2}")
#
# class Square(Rectangle):
#
#     def __init__(self, a):
#         super().__init__(a, a)
#     def get_S(self):
#         print(f"Площадь квадрата: {self.a ** 2}")
#
#     def get_P(self):
#         print(f"Периметр квадрата: {self.a * 4}")
#
# rec_1 = Rectangle(5, 7)
# sq_1 = Square(5)
# sq_1.get_P()
# rec_1.get_S()



#№22
# class Elevator:
#     def __init__(self, gr, max_gr):
#         self.gr = gr
#         self.max_gr = max_gr
#
#     def comparison(self):
#         if self.gr > self.max_gr:
#             print(f"Перегруз. Максимальное значение: {self.max_gr}, "
#                   f"текущее значение: {self.gr}")
#         elif self.gr < self.max_gr:
#             print(f"Недобор. Максимальное значение: {self.max_gr}, "
#                   f"текущее значение: {self.gr}")
#         elif self.gr == self.max_gr:
#             print(f"Лифт загружен до максимума. Максимальное значение: {self.max_gr}, "
#                   f"текущее значение: {self.gr}")
#
# el_1 = Elevator(590, 800)
# el_1.comparison()



#№34
# def decor(funk):
#     def wrapper(*args, **kwargs):
#         if args[1] > 4.5:
#             return funk(*args, **kwargs)
#     return wrapper
#
# @decor
# def func(name, osenk):
#     rez = "{:<8} | {:>4}"
#     return rez.format(name, osenk)
#
#
# rez = func("Egor", 4.7)
# if rez:
#     print(rez)
#
# rez = func("Dima", 4.4)
# if rez:
#     print(rez)



#№35
# def decor(func):
#     def wrapper(*args):
#         if args[0] % 2 == 0:
#             return func(*args) ** 2
#         elif args[0] % 2 != 0:
#             return func(*args) ** 3
#     return wrapper
#
# @decor
# def func(x):
#     return x
#
# print(func(9))
# print(func(4))



#№36
# def decor(func):
#     def wrapper(*args,**kwargs):
#         if args[0] <= args[1]:
#             return func(*args, **kwargs)
#         elif args[0] > args[1]:
#             result = args[0] - args[1]
#             return result
#     return wrapper
#
# @decor
# def summa(start,end):
#     cnt = 0
#     for i in range(start, end + 1):
#         cnt += i
#     return cnt
#
# print(summa(11, 10))



#№37
# def decor(func):
#     def wrapper(*args, **kwargs):
#         if None in kwargs.values():
#             return 0
#         else:
#             return func(*args, **kwargs)
#     return wrapper
#
# @decor
# def three_args(*, arg_1=None, arg_2=None, arg_3=None):
#     return arg_1 + arg_2 + arg_3
#
# print(three_args(arg_1=1, arg_2=3, arg_3=None))
# print(three_args(arg_1=1, arg_2=3, arg_3=7))



#№38
# def decor(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         if not result:
#             raise TypeError ("Результат вернул null")
#         return result
#     return wrapper
#
# @decor
# def funk(x):
#     return x
#
# print(funk(None))



#№39
