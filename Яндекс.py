class CipherMaster:
    def process_text(self, text, shift, is_encrypt):
        alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        result = ''

        if not is_encrypt:
            shift = -shift

        for char in text:
            lower_char = char.lower()

            if lower_char in alphabet:
                index = alphabet.index(lower_char)
                new_index = (index + shift) % len(alphabet)
                new_char = alphabet[new_index]

                if char.isupper():
                    result += new_char.upper()
                else:
                    result += new_char
            else:
                result += char

        return result

cipher_master = CipherMaster()

print(cipher_master.process_text(
    'Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
    2,
    True
))

print(cipher_master.process_text(
    'Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    -3,
    False
))

# class Employee:
#     vacation_days = 28
#
#     def __init__(self, first_name, second_name, gender):
#         self.first_name = first_name
#         self.second_name = second_name
#         self.gender = gender
#         self.remaining_vacation_days = Employee.vacation_days
#
#     def consume_vacation(self, days):
#         self.remaining_vacation_days -= days
#
#     def get_vacation_details(self):
#         return f'Остаток отпускных дней: {self.remaining_vacation_days}.'
#
#
# class FullTimeEmployee(Employee):
#
#     def get_unpaid_vacation(self, start_date, days):
#         return f'Начало неоплачиваемого отпуска: {start_date}, продолжительность: {days} дней.'
#
#
# class PartTimeEmployee(Employee):
#     vacation_days = 14
#
#     def __init__(self, first_name, second_name, gender):
#         super().__init__(first_name, second_name, gender)
#         self.remaining_vacation_days = PartTimeEmployee.vacation_days
#
#
# # Пример использования
#
# full_time_employee = FullTimeEmployee('Роберт', 'Крузо', 'м')
# print(full_time_employee.get_unpaid_vacation('2023-07-01', 5))
#
# part_time_employee = PartTimeEmployee('Алёна', 'Пятницкая', 'ж')
# print(part_time_employee.get_vacation_details())