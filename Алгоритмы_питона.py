# class BacteriaProducer:
#     # Допишите инициализатор класса
#     def __init__(self, max_bacteria = 10):
#         self.max_bacteria = max_bacteria
#         self.tek = 0
#
#
#     # Допишите метод
#     def create_new(self):
#         if self.tek < self.max_bacteria:
#             self.tek += 1
#             print(f" Добавлена одна бактерия. Количество бактерий в популяции: {self.tek}")
#         else:
#             print(f" Нет места под новую бактерию")
#
#     # Допишите метод
#     def remove_one(self):
#         if self.tek > 0:
#             self.tek -= 1
#             print(f"Одна бактерия удалена. Количество бактерий в популяции: {self.tek}")
#         else:
#             print(f" В популяции нет бактерий, удалять нечего")
#
# # Пример запуска для самопроверки
# bacteria_producer = BacteriaProducer(max_bacteria=3)
# bacteria_producer.remove_one()
# bacteria_producer.create_new()
# bacteria_producer.create_new()
# bacteria_producer.create_new()
# bacteria_producer.create_new()
# bacteria_producer.remove_one()
from pyparsing import alphas


# class MushroomsCollector:
#     # Проверьте, нет ли здесь ошибки:
#     mushrooms = []
#     def __init__(self):
#         self.mushrooms = []
#     # Исправьте ошибку в этом методе.
#     def is_poisonous(self, mushroom_name):
#         if mushroom_name == 'Мухомор' or mushroom_name == 'Поганка':
#             return True
#         return False
#
#     # Допишите метод.
#     def add_mushroom(self, mushroom_name):
#         if self.is_poisonous(mushroom_name):
#             print("Нельзя добавить ядовитый гриб")
#         else:
#             self.mushrooms.append(mushroom_name)
#
#     def __str__(self):
#         return ", ".join(self.mushrooms)
#     # Напишите магический метод __str__,
#     # возвращающий перечень грибов из списка mushrooms
#     # через запятую.
#
#
# # Пример запуска для самопроверки
# collector_1 = MushroomsCollector()
# collector_1.add_mushroom('Мухомор')
# collector_1.add_mushroom('Подосиновик')
# collector_1.add_mushroom('Белый')
# print(collector_1)
#
# collector_2 = MushroomsCollector()
# collector_2.add_mushroom('Лисичка')
# print(collector_1)
# print(collector_2)

class CipherMaster:
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def cipher(self, original_text, shift):
        # Метод должен возвращать зашифрованный текст
        # с учетом переданного смещения shift.
        pass

    def decipher(self, cipher_text, shift):
        dech = []
        for i in cipher_text:
            if i.isalpha():
                #print(i)
                i = i.lower()
                if self.alphabet.index(i) - shift > len(self.alphabet) - 1:
                    rez = self.alphabet.index(i) - shift - len(self.alphabet)
                    isk = self.alphabet[rez]
                    dech.append(isk)
                else:
                    new_ind = self.alphabet.index(i) - shift
                    new_b = self.alphabet[new_ind]
                    dech.append(new_b)

            else:
                dech.append(i)
        return "".join(dech)


        # Метод должен возвращать исходный текст
        # с учётом переданного смещения shift.
        ...


cipher_master = CipherMaster()
# print(cipher_master.cipher(
#     original_text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
#     shift=2
#))
print(cipher_master.decipher(
    cipher_text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3
))
