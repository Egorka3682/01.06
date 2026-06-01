class Permutation:
    def __init__(self, elements):
        """Инициализация перестановки."""
        self.elements = list(elements)
        self.size = len(set(elements))

        # Проверяем, является ли перестановкой
        if not self._is_valid_permutation():
            raise ValueError(
                f"Некорректная перестановка: {elements}. Должны быть числа от 1 до {self.size} без повторений")

    def _is_valid_permutation(self):
        """Проверяет, является ли список корректной перестановкой"""
        if not self.elements:
            return False

        # Проверяем, что все числа от 1 до n присутствуют ровно один раз
        seen = set()
        for num in self.elements:
            if num < 1 or num > self.size:
                return False
            if num in seen:
                return False
            seen.add(num)

        return len(seen) == self.size

    def __mul__(self, other):
        """Умножение перестановок (композиция): self * other (правильный порядок)"""
        if self.size != other.size:
            raise ValueError("Перестановки должны быть одного размера")

        result = [0] * self.size
        for i in range(self.size):
            result[i] = other.elements[self.elements[i] - 1]
        return Permutation(result)

    def inverse(self):
        """Нахождение обратной перестановки"""
        result = [0] * self.size
        for i in range(self.size):
            result[self.elements[i] - 1] = i + 1
        return Permutation(result)

    def __truediv__(self, other):
        """Деление перестановок: self / other = self*other^(-1)"""
        return self * other.inverse()

    def __str__(self):
        """Строковое представление в формате с индексами"""
        indices = " ".join(f"{i:2}" for i in range(1, self.size + 1))
        values = " ".join(f"{x:2}" for x in self.elements)
        return f"{indices}\n{values}"

    def __repr__(self):
        return f"Permutation({self.elements})"


def wrd_to_num(word):
    null = {'ноль': 0}
    units = {'один': 1, 'два': 2, 'три': 3, 'четыре': 4, 'пять': 5, 'шесть': 6, 'семь': 7, 'восемь': 8, 'девять': 9}
    teens = {'десять': 10, 'одиннадцать': 11, 'двенадцать': 12, 'тринадцать': 13, 'четырнадцать': 14, 'пятнадцать': 15,
             'шестнадцать': 16, 'семнадцать': 17, 'восемнадцать': 18, 'девятнадцать': 19}
    tens = {'двадцать': 20, 'тридцать': 30, 'сорок': 40, 'пятьдесят': 50, 'шестьдесят': 60, 'семьдесят': 70,
            'восемьдесят': 80, 'девяносто': 90}
    hundreds = {'сто': 100, 'двести': 200, 'триста': 300, 'четыреста': 400, 'пятьсот': 500, 'шестьсот': 600,
                'семьсот': 700, 'восемьсот': 800, 'девятьсот': 900}
    try:
        word = word.split()
    except:
        existing = -1
        return existing
    parts = []
    for part in word:
        check_part = [part for chck in [null, units, teens, tens, hundreds] if part in chck]
        if check_part != []:
            parts.append(part)
        else:
            existing = -1
            return existing
    if len(parts) == 2:
        if parts[0] in hundreds:
            if parts[1] not in tens and parts[1] not in teens and parts[1] not in units:
                existing = -1
                return existing
        elif parts[0] in tens:
            if parts[1] not in units:
                existing = -1
                return existing
        else:
            existing = -1
            return existing
    elif len(parts) == 3:
        if parts[0] not in hundreds or parts[1] not in tens or parts[2] not in units:
            existing = -1
            return existing
    elif len(parts) != 1:
        existing = -1
        return existing
    total_num = 0
    for part in parts:
        if part in null:
            total_num += null[part]
        elif part in units:
            total_num += units[part]
        elif part in teens:
            total_num += teens[part]
        elif part in tens:
            total_num += tens[part]
        elif part in hundreds:
            total_num += hundreds[part]
        else:
            existing = -1
            return existing
    return total_num


def text_to_numbers(text_input):
    """Преобразует текстовый ввод в числа"""

    def parse_number(word):
        """Парсит одно число из текста"""
        word = word.strip().lower()

        # Используем функцию wrd_to_num для преобразования
        num = wrd_to_num(word)
        if num == -1:
            raise ValueError(f"Неизвестное числовое слово: '{word}'. Используйте корректные числительные")

        return num

    # Разделяем ввод по запятым и обрабатываем каждое число
    words = [word.strip() for word in text_input.split(',')]
    numbers = []

    for word in words:
        if word:  # Пропускаем пустые строки
            numbers.append(parse_number(word))

    return numbers


def read_permutation(prompt, required_size=None):
    """Чтение перестановки из ввода пользователя"""
    print(prompt)
    print("Введите перестановку через запятую (например: 'один, два, три, четыре, пять'):")
    print("Можно использовать составные числа: 'двадцать один, тридцать пять'")

    if required_size:
        print(f"Размер перестановки должен быть {required_size}")

    while True:
        try:
            input_line = input().strip()
            if not input_line:
                continue

            # Преобразуем текстовый ввод в числа
            values = text_to_numbers(input_line)

            # Проверяем размер, если требуется
            if required_size and len(values) != required_size:
                raise ValueError(f"Размер перестановки должен быть {required_size}, а получено {len(values)}")

            perm = Permutation(values)
            return perm

        except ValueError as e:
            print(f"Ошибка: {e}")
            print("Попробуйте снова. Введите перестановку словами через запятую:")


def main():
    print("=== Калькулятор перестановок ===")

    # Чтение первой перестановки
    perm1 = read_permutation("Введите первую перестановку:")
    print(f"\nПервая перестановка:")
    print(perm1)

    # Чтение второй перестановки - теперь с проверкой размера
    perm2 = read_permutation("Введите вторую перестановку:", required_size=perm1.size)
    print(f"\nВторая перестановка:")
    print(perm2)

    while True:
        print("\nВыберите операцию:")
        print("умножение - умножить перестановки (первая * вторая)")
        print("деление - разделить перестановки (первая / вторая)")
        print("выход - завершить программу")

        choice = input("Ваш выбор: ").strip().lower()

        if choice == 'выход':
            break

        if choice == 'умножение':
            try:
                result = perm1 * perm2
                print(f"\nРезультат умножения:")
                print(result)
                print(f"\nВычисление: {perm1.elements} * {perm2.elements} = {result.elements}")

            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == 'деление':
            try:
                result = perm1 / perm2
                print(f"\nРезультат деления:")
                print(result)
                print(f"\nВычисление: {perm1.elements} / {perm2.elements} = {result.elements}")

            except ValueError as e:
                print(f"Ошибка: {e}")

        else:
            print("Неверная команда. Используйте 'умножение', 'деление' или 'выход'.")


if __name__ == "__main__":
    print("\n" + "=" * 50 + "\n")
    main()