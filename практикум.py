# class Permutation:
#     def __init__(self, elements):
#         """Инициализация перестановки."""
#         self.elements = list(elements)
#         self.size = len(elements)
#
#         # Проверяем, является ли перестановкой
#         if not self._is_valid_permutation():
#             raise ValueError(f"Некорректная перестановка: {elements}. Должны быть числа от 1 до {self.size} без повторений")
#
#     def _is_valid_permutation(self):
#         """Проверяет, является ли список корректной перестановкой"""
#         if not self.elements:
#             return False
#
#         # Проверяем, что все числа от 1 до n присутствуют ровно один раз
#         seen = set()
#         for num in self.elements:
#             if num < 1 or num > self.size:
#                 return False
#             if num in seen:
#                 return False
#             seen.add(num)
#
#         return len(seen) == self.size
#
#     def __mul__(self, other):
#         """Умножение перестановок (композиция): self * other (правильный порядок)"""
#         if self.size != other.size:
#             raise ValueError("Перестановки должны быть одного размера")
#
#         result = [0] * self.size
#         for i in range(self.size):
#             result[i] = other.elements[self.elements[i] - 1]
#         return Permutation(result)
#
#     def inverse(self):
#         """Нахождение обратной перестановки"""
#         result = [0] * self.size
#         for i in range(self.size):
#             result[self.elements[i] - 1] = i + 1
#         return Permutation(result)
#
#     def __truediv__(self, other):
#         """Деление перестановок: self / other = self*other^(-1)"""
#         return self * other.inverse()
#
#     def __str__(self):
#         """Строковое представление в формате с индексами"""
#         indices = " ".join(str(i) for i in range(1, self.size + 1))
#         values = " ".join(str(x) for x in self.elements)
#         return f"{indices}\n{values}"
#
#     def __repr__(self):
#         return f"Permutation({self.elements})"
#
# def read_permutation(prompt):
#     """Чтение перестановки из ввода пользователя"""
#     print(prompt)
#     print("Введите перестановку через пробел (например: 4 3 5 2 1):")
#
#     while True:
#         try:
#             input_line = input().strip()
#             if not input_line:
#                 continue
#
#             values = list(map(int, input_line.split()))
#             perm = Permutation(values)
#             return perm
#
#         except ValueError as e:
#             print(f"Ошибка: {e}")
#             print("Попробуйте снова. Введите перестановку через пробел:")
#
# def main():
#     print("=== Калькулятор перестановок ===")
#
#     # Чтение первой перестановки
#     perm1 = read_permutation("Введите первую перестановку:")
#     print(f"Первая перестановка:\n{perm1}")
#
#     # Чтение второй перестановки
#     perm2 = read_permutation("Введите вторую перестановку:")
#     print(f"Вторая перестановка:\n{perm2}")
#
#     while True:
#         print("\nВыберите операцию:")
#         print("умножение - умножить перестановки (первая * вторая)")
#         print("деление - разделить перестановки (первая / вторая)")
#         print("выход - завершить программу")
#
#         choice = input("Ваш выбор: ").strip().lower()
#
#         if choice == 'выход':
#             break
#
#         if choice == 'умножение':
#             try:
#                 result = perm1 * perm2
#                 print(f"\nРезультат умножения:")
#                 print(result)
#                 print(f"Вычисление: {perm1.elements} * {perm2.elements} = {result.elements}")
#
#             except ValueError as e:
#                 print(f"Ошибка: {e}")
#
#         elif choice == 'деление':
#             try:
#                 result = perm1 / perm2
#                 print(f"\nРезультат деления:")
#                 print(result)
#                 print(f"Вычисление: {perm1.elements} / {perm2.elements} = {result.elements}")
#
#             except ValueError as e:
#                 print(f"Ошибка: {e}")
#
#         else:
#             print("Неверная команда. Используйте 'умножение', 'деление' или 'выход'.")
#
# if __name__ == "__main__":
#
#     print("\n" + "="*50 + "\n")
#     main()

#1
s1 = 'папа принёс домой большую ёлку'
s = s1.split()
res = ''.join([i[0] for i in s])
print(res)
#2

import math
START = -math.pi
END = math.pi
step = 3
def drobi(start,end):
    chisla = []
    tekushiy = start
    while tekushiy <=end:
        chisla.append(tekushiy)
        tekushiy += step
        return chisla

A = [x for x in drobi(START,END)]
for x in A:
    y1 = 2*math.sin(x)
    y2 = math.cos(2*x)
    print(y1,y2)

#3
lst = [1, 2, 'a', 3, 4, 'b', 'c', 'd', 'e']
chars = [x for x in lst if type(x) == str]
print(chars)
numbers = [x for x in lst if type(x) == int][::-1]
print(numbers)
res = {chars[i]: numbers[i] if i < len(numbers) else 0 for i in range(len(chars))}
print(res)