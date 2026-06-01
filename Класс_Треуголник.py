import math
# КЛАСС ТОЧКИ

class Point:
    def __init__(self, x, y, z=None):
        self.__x = x
        self.__y = y
        self.__z = z

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def z(self):
        return self.__z

    def is_3d(self):
        return self.__z is not None

    def to_tuple(self):
        if self.is_3d():
            return (self.__x, self.__y, self.__z)
        return (self.__x, self.__y)

    def distance_to(self, other):
        if self.is_3d() and other.is_3d():
            return math.sqrt(
                (self.x - other.x) ** 2 +
                (self.y - other.y) ** 2 +
                (self.z - other.z) ** 2
            )
        return math.sqrt(
            (self.x - other.x) ** 2 +
            (self.y - other.y) ** 2
        )

    def __str__(self):
        if self.is_3d():
            return f"({self.x}, {self.y}, {self.z})"
        return f"({self.x}, {self.y})"

# БАЗОВЫЕ КЛАССЫ

class Figure:
    def area(self):
        raise NotImplementedError

    def perimeter(self):
        raise NotImplementedError

    def get_center(self):
        raise NotImplementedError

    def contains_origin(self):
        raise NotImplementedError


class FlatFigure(Figure):
    pass


class SpaceFigure(Figure):
    def volume(self):
        raise NotImplementedError

# ОКРУЖНОСТЬ

class Circle(FlatFigure):
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.__center = self.__calc_center()
        self.__radius = self.__calc_radius()

    def __calc_center(self):
        x1, y1 = self.p1.x, self.p1.y
        x2, y2 = self.p2.x, self.p2.y
        x3, y3 = self.p3.x, self.p3.y

        d = 2 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
        if d == 0:
            raise ValueError("Точки лежат на одной прямой")

        ux = (
            (x1 ** 2 + y1 ** 2) * (y2 - y3) +
            (x2 ** 2 + y2 ** 2) * (y3 - y1) +
            (x3 ** 2 + y3 ** 2) * (y1 - y2)
        ) / d

        uy = (
            (x1 ** 2 + y1 ** 2) * (x3 - x2) +
            (x2 ** 2 + y2 ** 2) * (x1 - x3) +
            (x3 ** 2 + y3 ** 2) * (x2 - x1)
        ) / d

        return Point(ux, uy)

    def __calc_radius(self):
        return self.__center.distance_to(self.p1)

    @property
    def radius(self):
        return self.__radius

    def area(self):
        return math.pi * self.__radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.__radius

    def get_center(self):
        return self.__center

    def contains_origin(self):
        origin = Point(0, 0)
        return self.__center.distance_to(origin) <= self.__radius

    def __str__(self):
        return f"Окружность | Центр: {self.__center} | Радиус: {self.__radius}"

# ТРЕУГОЛЬНИК

class Triangle(FlatFigure):
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        if self.area() == 0:
            raise ValueError("Точки лежат на одной прямой")

    def area(self):
        x1, y1 = self.p1.x, self.p1.y
        x2, y2 = self.p2.x, self.p2.y
        x3, y3 = self.p3.x, self.p3.y
        return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2)

    def perimeter(self):
        return (
            self.p1.distance_to(self.p2) +
            self.p2.distance_to(self.p3) +
            self.p3.distance_to(self.p1)
        )

    def get_center(self):
        return Point(
            (self.p1.x + self.p2.x + self.p3.x) / 3,
            (self.p1.y + self.p2.y + self.p3.y) / 3
        )

    def contains_origin(self):
        return self.__inside(Point(0, 0))

    def __inside(self, p):
        def sign(a, b, c):
            return (a.x - c.x) * (b.y - c.y) - (b.x - c.x) * (a.y - c.y)

        b1 = sign(p, self.p1, self.p2) < 0
        b2 = sign(p, self.p2, self.p3) < 0
        b3 = sign(p, self.p3, self.p1) < 0
        return b1 == b2 == b3

    def __str__(self):
        return f"Треугольник | Центр: {self.get_center()}"

# ПРЯМОУГОЛЬНЫЙ ПАРАЛЛЕЛЕПИПЕД

class Parallelepiped(SpaceFigure):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

        if self.length() == 0 or self.width() == 0 or self.height() == 0:
            raise ValueError("Параллелепипед должен иметь ненулевые размеры")

    def length(self):
        return abs(self.p2.x - self.p1.x)

    def width(self):
        return abs(self.p2.y - self.p1.y)

    def height(self):
        return abs(self.p2.z - self.p1.z)

    def area(self):
        a = self.length()
        b = self.width()
        c = self.height()
        return 2 * (a * b + a * c + b * c)

    def perimeter(self):
        a = self.length()
        b = self.width()
        c = self.height()
        return 4 * (a + b + c)

    def volume(self):
        return self.length() * self.width() * self.height()

    def get_center(self):
        return Point(
            (self.p1.x + self.p2.x) / 2,
            (self.p1.y + self.p2.y) / 2,
            (self.p1.z + self.p2.z) / 2
        )

    def contains_origin(self):
        min_x, max_x = sorted([self.p1.x, self.p2.x])
        min_y, max_y = sorted([self.p1.y, self.p2.y])
        min_z, max_z = sorted([self.p1.z, self.p2.z])

        return (
            min_x <= 0 <= max_x and
            min_y <= 0 <= max_y and
            min_z <= 0 <= max_z
        )

    def __str__(self):
        return f"Параллелепипед | Центр: {self.get_center()} | Объем: {self.volume()}"

# МЕНЕДЖЕР ФИГУР

class FigureManager:
    def __init__(self):
        self.figures = []

    def add(self, figure):
        self.figures.append(figure)

    def total_area(self):
        return sum(fig.area() for fig in self.figures)

    def total_perimeter(self):
        return sum(fig.perimeter() for fig in self.figures)

    def sum_centers(self):
        first = self.figures[0].get_center()
        if first.is_3d():
            sx = sum(fig.get_center().x for fig in self.figures)
            sy = sum(fig.get_center().y for fig in self.figures)
            sz = sum(fig.get_center().z for fig in self.figures)
            return Point(sx, sy, sz)
        else:
            sx = sum(fig.get_center().x for fig in self.figures)
            sy = sum(fig.get_center().y for fig in self.figures)
            return Point(sx, sy)

    def count_with_origin(self):
        return sum(fig.contains_origin() for fig in self.figures)

    def total_volume(self):
        total = 0
        for fig in self.figures:
            if isinstance(fig, SpaceFigure):
                total += fig.volume()
        return total

# ВВОД

def read_number(prompt):
    print('Для выхода введите "ВЫХОД"')
    value = input(prompt).strip()
    if value.lower() == "выход":
        return "exit"
    if "," in value:
        raise ValueError("Используйте точку, а не запятую")
    return float(value)


def read_int(prompt):
    print('Для выхода введите "ВЫХОД"')
    value = input(prompt).strip()
    if value.lower() == "выход":
        return "exit"
    if not value.isdigit():
        raise ValueError("Введите целое число")
    return int(value)


def read_2d_points():
    nums = []
    for name in ["x1", "y1", "x2", "y2", "x3", "y3"]:
        val = read_number(f"Введите {name}: ")
        if val == "exit":
            return "exit"
        nums.append(val)

    return Point(nums[0], nums[1]), Point(nums[2], nums[3]), Point(nums[4], nums[5])


def read_3d_points():
    nums = []
    for name in ["x1", "y1", "z1", "x2", "y2", "z2"]:
        val = read_number(f"Введите {name}: ")
        if val == "exit":
            return "exit"
        nums.append(val)

    return Point(nums[0], nums[1], nums[2]), Point(nums[3], nums[4], nums[5])

# СОЗДАНИЕ ФИГУРЫ

def create_figure(figure_type, data):
    if figure_type == 1:
        p1, p2, p3 = data
        return Circle(p1, p2, p3)
    elif figure_type == 2:
        p1, p2, p3 = data
        return Triangle(p1, p2, p3)
    elif figure_type == 3:
        p1, p2 = data
        return Parallelepiped(p1, p2)
    else:
        raise ValueError("Неизвестный тип фигуры")

# МЕНЮ ОДНОЙ ФИГУРЫ

def one_figure_menu(fig):
    while True:
        print('\nДля выхода введите "ВЫХОД"')
        print('Для возврата введите "НАЗАД"')
        print("1) Площадь")
        print("2) Периметр")
        print("3) Центр")
        print("4) Проверить, содержит ли начало координат")

        if isinstance(fig, Circle):
            print("5) Радиус")
        if isinstance(fig, SpaceFigure):
            print("6) Объем")

        choice = input("Ваш выбор: ").strip().lower()

        if choice == "выход":
            return "exit"
        if choice == "назад":
            return

        if choice == "1":
            print("Площадь:", fig.area())
        elif choice == "2":
            print("Периметр:", fig.perimeter())
        elif choice == "3":
            print("Центр:", fig.get_center())
        elif choice == "4":
            print("Содержит начало координат:", fig.contains_origin())
        elif choice == "5" and isinstance(fig, Circle):
            print("Радиус:", fig.radius)
        elif choice == "6" and isinstance(fig, SpaceFigure):
            print("Объем:", fig.volume())
        else:
            print("Ошибка выбора")

# МЕНЮ ВСЕХ ФИГУР

def all_figures_menu(manager):
    while True:
        print('\nДля выхода введите "ВЫХОД"')
        print('Для возврата введите "НАЗАД"')
        print("1) Суммарная площадь")
        print("2) Суммарный периметр")
        print("3) Сумма центров")
        print("4) Сколько фигур содержат начало координат")

        has_3d = any(isinstance(fig, SpaceFigure) for fig in manager.figures)
        if has_3d:
            print("5) Суммарный объем")

        choice = input("Ваш выбор: ").strip().lower()

        if choice == "выход":
            return "exit"
        if choice == "назад":
            return

        if choice == "1":
            print("Суммарная площадь:", manager.total_area())
        elif choice == "2":
            print("Суммарный периметр:", manager.total_perimeter())
        elif choice == "3":
            print("Сумма центров:", manager.sum_centers())
        elif choice == "4":
            print("Количество фигур:", manager.count_with_origin())
        elif choice == "5" and has_3d:
            print("Суммарный объем:", manager.total_volume())
        else:
            print("Ошибка выбора")

# КОНСОЛЬНЫЙ РЕЖИМ

def case_console():
    manager = FigureManager()

    print("Выберите тип фигуры:")
    print("1) Окружность")
    print("2) Треугольник")
    print("3) Параллелепипед")

    figure_type = input("Ваш выбор: ").strip().lower()
    if figure_type == "выход":
        return
    if figure_type not in ("1", "2", "3"):
        print("Ошибка выбора")
        return

    figure_type = int(figure_type)

    try:
        n = read_int("Сколько фигур будет? ")
        if n == "exit":
            return
    except ValueError as e:
        print(e)
        return

    for i in range(n):
        print(f"\nВвод фигуры #{i + 1}")
        try:
            if figure_type in (1, 2):
                data = read_2d_points()
            else:
                data = read_3d_points()

            if data == "exit":
                return

            manager.add(create_figure(figure_type, data))
        except ValueError as e:
            print("Ошибка:", e)
            return

    while True:
        print('\nДля выхода введите "ВЫХОД"')
        print("1) Работать со всем набором")
        print("2) Работать с одной фигурой")

        mode = input("Ваш выбор: ").strip().lower()

        if mode == "выход":
            return
        elif mode == "1":
            result = all_figures_menu(manager)
            if result == "exit":
                return
        elif mode == "2":
            for i, fig in enumerate(manager.figures, 1):
                print(f"{i}) {fig}")

            num = input('Выберите номер фигуры или "ВЫХОД": ').strip().lower()
            if num == "выход":
                return
            if not num.isdigit():
                print("Ошибка номера")
                continue

            num = int(num)
            if not (1 <= num <= len(manager.figures)):
                print("Такой фигуры нет")
                continue

            result = one_figure_menu(manager.figures[num - 1])
            if result == "exit":
                return
        else:
            print("Ошибка выбора")

# РЕЖИМ ФАЙЛА

def case_file():
    manager = FigureManager()

    with open("input.txt", "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    figure_type = int(lines[1])
    mode = int(lines[2])

    if mode == 1:
        operation = int(lines[3])
        data_lines = lines[4:]
    else:
        fig_num = int(lines[3])
        operation = int(lines[4])
        data_lines = lines[5:]

    for line in data_lines:
        nums = list(map(float, line.split()))

        if figure_type in (1, 2):
            if len(nums) != 6:
                raise ValueError("Для 2D фигуры нужно 6 чисел")
            data = (
                Point(nums[0], nums[1]),
                Point(nums[2], nums[3]),
                Point(nums[4], nums[5])
            )
        else:
            if len(nums) != 6:
                raise ValueError("Для параллелепипеда нужно 6 чисел")
            data = (
                Point(nums[0], nums[1], nums[2]),
                Point(nums[3], nums[4], nums[5])
            )

        manager.add(create_figure(figure_type, data))

    if mode == 1:
        if operation == 1:
            result = manager.total_area()
        elif operation == 2:
            result = manager.total_perimeter()
        elif operation == 3:
            result = manager.sum_centers()
        elif operation == 4:
            result = manager.count_with_origin()
        elif operation == 5:
            result = manager.total_volume()
        else:
            raise ValueError("Неизвестная операция")
    else:
        fig = manager.figures[fig_num - 1]

        if operation == 1:
            result = fig.area()
        elif operation == 2:
            result = fig.perimeter()
        elif operation == 3:
            result = fig.get_center()
        elif operation == 4:
            result = fig.contains_origin()
        elif operation == 5 and isinstance(fig, Circle):
            result = fig.radius
        elif operation == 6 and isinstance(fig, SpaceFigure):
            result = fig.volume()
        else:
            raise ValueError("Неизвестная операция")

    with open("result.txt", "w", encoding="utf-8") as f:
        f.write(str(result))

    print("Результат записан в result.txt")

# ЗАПУСК

def main():
    try:
        with open("input.txt", "r", encoding="utf-8") as f:
            first = f.readline().strip()

        if first == "1":
            case_file()
        else:
            case_console()
    except FileNotFoundError:
        case_console()
    except Exception as e:
        print("Ошибка:", e)


if __name__ == "__main__":
    main()