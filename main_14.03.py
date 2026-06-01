# class Sportsman:
#     def __init__(self, name, surname, age):
#         self.name = name
#         self.surname = surname
#         self.age = age
#
#     def matches_name(self, name):
#         return self.name.lower() == name.lower()
#
#     def matches_age(self, age):
#         return self.age == age
#
#     def __str__(self):
#         return f'{self.name} {self.surname}, возраст: {self.age}'
#
#
# class Athlete(Sportsman):
#     def __init__(self, name, surname, age, discipline):
#         super().__init__(name, surname, age)
#         self.discipline = discipline
#
#     def __str__(self):
#         return f'Легкоатлет: {self.name} {self.surname}, возраст: {self.age}, дисциплина: {self.discipline}'
#
#
# class Swimmer(Sportsman):
#     def __init__(self, name, surname, age, distance):
#         super().__init__(name, surname, age)
#         self.distance = distance
#
#     def __str__(self):
#         return f'Пловец: {self.name} {self.surname}, возраст: {self.age}, дистанция: {self.distance}'
#
#
# class Boxer(Sportsman):
#     def __init__(self, name, surname, age, weight_category):
#         super().__init__(name, surname, age)
#         self.weight_category = weight_category
#
#     def __str__(self):
#         return f'Боксер: {self.name} {self.surname}, возраст: {self.age}, весовая категория: {self.weight_category}'
#
#
# sportsmen = [
#     Athlete('Иван', 'Петров', 20, 'бег 100 м'),
#     Swimmer('Анна', 'Сидорова', 18, '200 м'),
#     Boxer('Олег', 'Иванов', 22, 'средний вес'),
#     Athlete('Анна', 'Кузнецова', 19, 'прыжки в длину')
# ]
#
# print('Полная информация о спортсменах:')
# for sportsman in sportsmen:
#     print(sportsman)
#
# search_name = 'Иван'
# print(f'\nПоиск по имени "{search_name}":')
# for sportsman in sportsmen:
#     if sportsman.matches_name(search_name):
#         print(sportsman)
#
# search_age = 20
# print(f'\nПоиск по возрасту {search_age}:')
# for sportsman in sportsmen:
#     if sportsman.matches_age(search_age):
#         print(sportsman)

# class Board:
#
#     def __init__(self):
#         # создаём поле 3x3
#         self.board = [[' ' for _ in range(3)] for _ in range(3)]
#
#     def make_move(self, row, col, symbol):
#         # размещаем символ
#         self.board[row][col] = symbol
#
#     def display(self):
#         for row in self.board:
#             print('|'.join(row))
#             print('-----')
#
#
# # создание игрового поля
# game = Board()
#
# # вывод пустого поля
# game.display()
#
# # ход игрока
# game.make_move(1, 1, 'X')
#
# print('Ход сделан!\n')
#
# # вывод поля после хода
# game.display()
#
# game.make_move(0, 0, 'X')
#
# print('Ход сделан!\n')
#
# game.display()

# from datetime import datetime
#
#
# class Workers:
#     def __init__(self, company_name, qualification, name):
#         self.company_name = company_name
#         self.qualification = qualification
#         self.name = name
#
#     def __str__(self):
#         return f'{self.name}, {self.qualification}, компания: {self.company_name}'
#
#
# class House:
#     def __init__(self, floors, entrances, district, workers, start_date, end_date):
#         self.floors = floors
#         self.entrances = entrances
#         self.district = district
#         self.workers = workers
#         self.start_date = datetime.strptime(start_date, '%d.%m.%Y')
#         self.end_date = datetime.strptime(end_date, '%d.%m.%Y')
#
#     def __str__(self):
#         workers_info = ', '.join(worker.name for worker in self.workers)
#         return (f'Дом: {self.floors} этаж(ей), {self.entrances} подъезд(ов), '
#                 f'район: {self.district}, '
#                 f'сроки: {self.start_date.strftime("%d.%m.%Y")} - {self.end_date.strftime("%d.%m.%Y")}, '
#                 f'рабочие: {workers_info}')
#
#
# def count_worker_projects_in_year(worker, houses, year):
#     count = 0
#     for house in houses:
#         if worker in house.workers:
#             if house.start_date.year <= year <= house.end_date.year:
#                 count += 1
#     return count
#
#
# # Рабочие
# worker1 = Workers('СтройМир', 'каменщик', 'Иван')
# worker2 = Workers('СтройМир', 'сварщик', 'Петр')
# worker3 = Workers('ДомСтрой', 'крановщик', 'Анна')
#
# # Дома
# house1 = House(9, 3, 'Центральный', [worker1, worker2], '01.01.2022', '01.12.2022')
# house2 = House(12, 4, 'Северный', [worker1, worker3], '15.03.2022', '20.08.2023')
# house3 = House(5, 2, 'Южный', [worker2, worker3], '10.01.2023', '10.10.2023')
#
# houses = [house1, house2, house3]
#
# # Вывод информации о домах
# for house in houses:
#     print(house)
#
# print()
#
# # Проверка: в скольких постройках рабочий задействован в 2022 году
# print(f'{worker1.name} задействован в {count_worker_projects_in_year(worker1, houses, 2022)} постройках в 2022 году.')
# print(f'{worker2.name} задействован в {count_worker_projects_in_year(worker2, houses, 2022)} постройках в 2022 году.')
# print(f'{worker3.name} задействован в {count_worker_projects_in_year(worker3, houses, 2022)} постройках в 2022 году.')

# class Drob:
#     def __init__(self, name):
#         self.name = name
#
#     def __add__(self, other):
#         dr1 = self.name.split('/')
#         dr2 = other.name.split('/')
#         res_ch = int(dr1[0]) + int(dr2[0])
#         res_zn = dr1[1]
#         return str(res_ch) + '/' + res_zn
#
#     def __sub__(self, other):
#         dr1 = self.name.split('/')
#         dr2 = other.name.split('/')
#         res_ch = int(dr1[0]) - int(dr2[0])
#         res_zn = dr1[1]
#         return str(res_ch) + '/' + res_zn
#
#     def __mul__(self, other):
#         dr1 = self.name.split('/')
#         dr2 = other.name.split('/')
#         res_ch = int(dr1[0]) * int(dr2[0])
#         res_zn = int(dr1[-1]) * int(dr2[-1])
#         return str(res_ch) + '/' + str(res_zn)
#
#
#
#
# d1 = Drob('2/4')
# d2 = Drob('3/4')
# print(d1.__dict__)
# print(d1 + d2)
# print(d1 - d2)
# print(d1 * d2)

class CipherMaster:
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def cipher(self, original_text, shift):
        # Метод должен возвращать зашифрованный текст
        # с учетом переданного смещения shift.
        self.result = []
        self.original_text = original_text
        self.self = shift
        original_text = original_text.lower()
        for i in original_text:
                if i in self.alphabet:
                    if i.isupper() == True:
                        new_index = (self.alphabet.index(i) + shift) % len(self.alphabet)
                        new_letter = self.alphabet[new_index]
                        self.result.append(new_letter.upper())
                    else:
                        new_index = (self.alphabet.index(i) + shift) % len(self.alphabet)
                        new_letter = self.alphabet[new_index]
                        self.result.append(new_letter)

                else:
                    self.result.append(i)
        return ''.join(self.result)

    def decipher(self, cipher_text, shift):
        # Метод должен возвращать исходный текст
        # с учётом переданного смещения shift.
        self.result = []
        self.cipher_text = cipher_text
        self.self = shift
        cipher_text = cipher_text.lower()
        for i in cipher_text:
            if i in self.alphabet:
                new_index = (self.alphabet.index(i) - shift) % len(self.alphabet)
                new_letter = self.alphabet[new_index]
                self.result.append(new_letter)
            else:
                self.result.append(i)
        return ''.join(self.result)


cipher_master = CipherMaster()
print(cipher_master.cipher(
    original_text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
    shift=2
))
print(cipher_master.decipher(
    cipher_text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3
))