# class Employee:
#     def __init__(self, last_name, first_name, position, salary):
#         self.last_name = last_name
#         self.first_name = first_name
#         self.position = position
#         self.salary = salary
#         self.experience = 0
#
#     def set_experience(self, experience):
#         self.experience = experience
#
#     def is_high_salary(self):
#         return self.salary > 100000
#
#     def __str__(self):
#         return (f"Фамилия: {self.last_name}\n"
#                 f"Имя: {self.first_name}\n"
#                 f"Должность: {self.position}\n"
#                 f"Зарплата: {self.salary} руб.\n"
#                 f"Стаж работы: {self.experience} лет")
#
#
# employee1 = Employee("Иванов", "Иван", "Менеджер", 120000)
# employee1.set_experience(6)
#
# print(employee1)
# print("Высокая зарплата:", employee1.is_high_salary())

# class Employee:
#     def __init__(self, surname, name, dol, money):
#         self.surname = surname
#         self.name = name
#         self.dol = dol
#         self.money = money
#         self.__work = 6
#     def high_mon(self):
#         if self.money > 100000:
#             return 'зарплата высокая'
#         else:
#             return 'зарплата низкая'
#     def __str__(self):
#         return f'Сотрудник с именем {self.name} и фамилией {self.surname} работает на должности {self.dol} с зарплатой {self.money}'
#
#     @property
#     def work(self):
#         return self.__work
#
#     @work.setter
#     def work(self, new):
#         self.__work = new
#
# w = Employee('Петров', 'Петр', 'начальник', 200000)
# print(w)
# print(w.high_mon())
# print(w.work)
# w.work = 10
# print(w.work)

# class Employee:
#     def __init__(self, surname, name, dol, money):
#         self.surname = surname
#         self.name = name
#         self.dol = dol
#         self.money = money
#         self.__work = 6
#     def high_mon(self):
#         if self.money > 100000:
#             return 'зарплата высокая'
#         else:
#             return 'зарплата низкая'
#     def __str__(self):
#         return f'Сотрудник с именем {self.name} и фамилией {self.surname} работает на должности {self.dol} с зарплатой {self.money}'
#
#     def __get_r(self):
#         return self.__work
#
#     def __set_w(self, new):
#         self.__work = new
#
#     work = property(__get_r, __set_w)
#
# w = Employee('Петров', 'Петр', 'начальник', 200000)
# print(w)
# print(w.high_mon())
# print(w.work)
# w.work = 10
# print(w.work)

# class Avto:
#     def __init__(self, mark, model, year):
#         self.mark = mark
#         self.model = model
#         self.year = year
#
#     def __str__(self):
#         return (f'Марка автомобиля: {self.mark}\n'
#                 f'Можель автомобиля: {self.model}\n'
#                 f'Год выпуска: {self.year}')
# class Passenger(Avto):
#     def __init__(self, mark, model, year, body_type):
#         super().__init__(mark, model, year)
#         self.body_type = body_type
#     def __str__(self):
#         return f'{super().__str__()}\nТип кузова: {self.body_type}'
#
# class Cargo(Avto):
#     def __init__(self, mark, model, year, load_capacity):
#         super().__init__(mark, model, year)
#         self.load_capacity = load_capacity
#     def __str__(self):
#         return f'{super().__str__()}\nГрузоподъёмность: {self.load_capacity}'
# car = Avto('Toyota', "Mark_2", 1980)
# car_1 = Passenger('Toyota', "Mark_2", 1980, "седан")
# car_2 = Cargo("Белаз", "новый", 2008, "180 тон")
# print(car)
# print(car_1)
# print(car_2)

# class Employee:
#     vacation_days = 28
#
#     def __init__(self, first_name, second_name, gender):
#         self.first_name = first_name
#         self.second_name = second_name
#         self.gender = gender
#         self.remaining_vacation_days = Employee.vacation_days
#
#         # защищённый атрибут
#         self._employee_id = self.__generate_employee_id()
#
#     # приватный метод
#     def __generate_employee_id(self):
#         data = self.first_name + self.second_name + self.gender
#         return hash(data)
#
#     def consume_vacation(self, days):
#         self.remaining_vacation_days -= days
#
#     def get_vacation_details(self):
#         return f'Остаток отпускных дней: {self.remaining_vacation_days}.'
#
#     def get_employee_id(self):
#         return f'ID сотрудника: {self._employee_id}'
#
#
# class FullTimeEmployee(Employee):
#     def __init__(self, first_name, second_name, gender, salary):
#         super().__init__(first_name, second_name, gender)
#
#         # приватный атрибут
#         self.__salary = salary
#
#     # приватный метод
#     def __get_vacation_salary(self):
#         return self.__salary * 0.8
#
#     def get_vacation_payment(self):
#         return f'Отпускные выплаты: {self.__get_vacation_salary()}'
#
#     def get_unpaid_vacation(self, start_date, days):
#         return f'Начало неоплачиваемого отпуска: {start_date}, продолжительность: {days} дней.'
#
#
# class PartTimeEmployee(Employee):
#     pass
#
#
# # Пример использования:
# full_time_employee = FullTimeEmployee('Иван', 'Иванов', 'м', 50000)
# print(full_time_employee.get_unpaid_vacation('2023-07-01', 5))
# print(full_time_employee.get_vacation_payment())
# print(full_time_employee.get_employee_id())
#
# part_time_employee = PartTimeEmployee('Анна', 'Петрова', 'ж')
# part_time_employee.consume_vacation(5)
# print(part_time_employee.get_vacation_details())
# print(part_time_employee.get_employee_id())

class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def get_info(self):
        return f'{self.name} (в наличии: {self.quantity})'


class Kettlebell(Product):
    def __init__(self, name, quantity, weight):
        super().__init__(name, quantity)
        self.weight = weight

    def get_weight(self):
        return f'{self.get_info()}. Вес: {self.weight} кг'


class Clothing(Product):
    def __init__(self, name, quantity, size):
        super().__init__(name, quantity)
        self.size = size

    def get_size(self):
        return f'{self.get_info()}. Размер: {self.size}'


# Для проверки:
small_kettlebell = Kettlebell('Гиря малая', 15, 2)
shirt = Clothing('Футболка', 5, 'L')

print(small_kettlebell.get_weight())
print(shirt.get_size())
