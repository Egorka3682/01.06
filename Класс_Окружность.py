import math


class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def to_tuple(self):
        return self.__x, self.__y

    def __repr__(self):
        return f"({self.__x}, {self.__y})"


def read_value(prompt, value_type=float):
    print('Для выхода введите "ВЫХОД"')
    value = input(prompt).strip()

    if value.lower() == "выход":
        return "exit"

    if value_type == float and "," in value:
        raise ValueError("Ошибка: используйте точку, а не запятую")

    return value_type(value)


def read_points():
    coords = []
    names = ["x1", "y1", "x2", "y2", "x3", "y3"]

    for name in names:
        val = read_value(f"Введите {name}: ", float)
        if val == "exit":
            return "exit"
        coords.append(val)

    p1 = Point(coords[0], coords[1])
    p2 = Point(coords[2], coords[3])
    p3 = Point(coords[4], coords[5])

    return p1, p2, p3


class GeometricFigure:
    def area(self):
        raise NotImplementedError

    def perimeter(self):
        raise NotImplementedError

    def get_center(self):
        raise NotImplementedError

    def contains_origin(self):
        raise NotImplementedError


class Circle(GeometricFigure):
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.center = self._calc_center()
        self.radius = self._calc_radius()

    def _calc_center(self):
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

    def _calc_radius(self):
        cx, cy = self.center.x, self.center.y
        x1, y1 = self.p1.x, self.p1.y
        return math.sqrt((x1 - cx) ** 2 + (y1 - cy) ** 2)

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def get_center(self):
        return self.center

    def contains_origin(self):
        cx, cy = self.center.x, self.center.y
        return math.sqrt(cx ** 2 + cy ** 2) <= self.radius


class Triangle(GeometricFigure):
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

        if self.area() == 0:
            raise ValueError("Точки лежат на одной прямой")

    def _dist(self, a, b):
        return math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)

    def area(self):
        x1, y1 = self.p1.x, self.p1.y
        x2, y2 = self.p2.x, self.p2.y
        x3, y3 = self.p3.x, self.p3.y

        return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2)

    def perimeter(self):
        return (
            self._dist(self.p1, self.p2) +
            self._dist(self.p2, self.p3) +
            self._dist(self.p3, self.p1)
        )

    def get_center(self):
        return Point(
            (self.p1.x + self.p2.x + self.p3.x) / 3,
            (self.p1.y + self.p2.y + self.p3.y) / 3
        )

    def contains_origin(self):
        return self._inside(Point(0, 0))

    def _inside(self, p):
        def sign(a, b, c):
            return (a.x - c.x) * (b.y - c.y) - (b.x - c.x) * (a.y - c.y)

        b1 = sign(p, self.p1, self.p2) < 0
        b2 = sign(p, self.p2, self.p3) < 0
        b3 = sign(p, self.p3, self.p1) < 0

        return b1 == b2 == b3


class FigureManager:
    def __init__(self):
        self.figures = []

    def add(self, figure):
        self.figures.append(figure)

    def total_area(self):
        return sum(f.area() for f in self.figures)

    def total_perimeter(self):
        return sum(f.perimeter() for f in self.figures)

    def sum_centers(self):
        return (
            sum(f.get_center().x for f in self.figures),
            sum(f.get_center().y for f in self.figures)
        )

    def count_with_origin(self):
        return sum(f.contains_origin() for f in self.figures)


def create_figure(figure_type, p1, p2, p3):
    if figure_type == 1:
        return Circle(p1, p2, p3)
    return Triangle(p1, p2, p3)


def show_actions(is_circle):
    print("\n1) Площадь")
    print("2) Периметр")
    print("3) Центр")
    print("4) Проверить, содержит ли (0,0)")
    if is_circle:
        print("5) Радиус")
    print('Для выхода введите "ВЫХОД"')
    print('Для возврата введите "НАЗАД"')


def apply_to_one(figure, is_circle):
    while True:
        show_actions(is_circle)
        choice = input("Ваш выбор: ").strip().lower()

        if choice == "выход":
            return "exit"
        if choice == "назад":
            return

        if choice == "1":
            print("Площадь:", figure.area())
        elif choice == "2":
            print("Периметр:", figure.perimeter())
        elif choice == "3":
            print("Центр:", figure.get_center())
        elif choice == "4":
            print("Содержит (0,0):", figure.contains_origin())
        elif choice == "5" and is_circle:
            print("Радиус:", figure.radius)
        else:
            print("Ошибка выбора.")


def apply_to_all(manager):
    while True:
        print("\n1) Суммарная площадь")
        print("2) Суммарный периметр")
        print("3) Сумма координат центров")
        print("4) Сколько фигур содержат (0,0)")
        print('Для выхода введите "ВЫХОД"')
        print('Для возврата введите "НАЗАД"')

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
            print("Сумма координат центров:", manager.sum_centers())
        elif choice == "4":
            print("Количество фигур:", manager.count_with_origin())
        else:
            print("Ошибка выбора.")


def case_console():
    manager = FigureManager()

    print('Для выхода введите "ВЫХОД"')
    print("\nВыберите тип фигуры:")
    print("1) Окружность")
    print("2) Треугольник")

    figure_type = input("Ваш выбор: ").strip().lower()
    if figure_type == "выход":
        return
    if figure_type not in ("1", "2"):
        print("Ошибка выбора.")
        return

    figure_type = int(figure_type)
    is_circle = figure_type == 1

    try:
        n = read_value("Сколько будет фигур? ", int)
        if n == "exit":
            return
        if n <= 0:
            print("Количество должно быть больше нуля.")
            return
    except ValueError:
        print("Ошибка ввода количества.")
        return

    for i in range(n):
        print(f"\nВвод фигуры #{i + 1}")
        try:
            points = read_points()
            if points == "exit":
                return
            p1, p2, p3 = points
            manager.add(create_figure(figure_type, p1, p2, p3))
        except ValueError as e:
            print("Ошибка:", e)
            return

    while True:
        print("\n1) Работать со всем списком")
        print("2) Работать с одной фигурой")
        print('Для выхода введите "ВЫХОД"')

        mode = input("Ваш выбор: ").strip().lower()

        if mode == "выход":
            return

        if mode == "1":
            result = apply_to_all(manager)
            if result == "exit":
                return

        elif mode == "2":
            for i, fig in enumerate(manager.figures, 1):
                if is_circle:
                    print(f"{i}) Окружность | Центр: {fig.get_center()} | Радиус: {fig.radius}")
                else:
                    print(f"{i}) Треугольник | Центр: {fig.get_center()}")

            num = input('Выберите номер фигуры или "ВЫХОД": ').strip().lower()
            if num == "выход":
                return
            if not num.isdigit():
                print("Ошибка номера.")
                continue

            num = int(num)
            if not (1 <= num <= len(manager.figures)):
                print("Такой фигуры нет.")
                continue

            result = apply_to_one(manager.figures[num - 1], is_circle)
            if result == "exit":
                return
        else:
            print("Ошибка выбора.")


def case_file():
    manager = FigureManager()

    with open("input.txt", "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    figure_type = int(lines[1])
    mode = int(lines[2])

    if mode == 1:
        operation = int(lines[3])
        data = lines[4:]
    else:
        index_figure = int(lines[3])
        operation = int(lines[4])
        data = lines[5:]

    for line in data:
        nums = list(map(float, line.split()))
        p1 = Point(nums[0], nums[1])
        p2 = Point(nums[2], nums[3])
        p3 = Point(nums[4], nums[5])
        manager.add(create_figure(figure_type, p1, p2, p3))

    if mode == 1:
        if operation == 1:
            result = manager.total_area()
        elif operation == 2:
            result = manager.total_perimeter()
        elif operation == 3:
            result = manager.sum_centers()
        elif operation == 4:
            result = manager.count_with_origin()
        else:
            raise ValueError("Неизвестная операция")
    else:
        fig = manager.figures[index_figure - 1]

        if operation == 1:
            result = fig.area()
        elif operation == 2:
            result = fig.perimeter()
        elif operation == 3:
            result = fig.get_center()
        elif operation == 4:
            result = fig.contains_origin()
        elif operation == 5 and figure_type == 1:
            result = fig.radius
        else:
            raise ValueError("Неизвестная операция")

    with open("result.txt", "w", encoding="utf-8") as f:
        f.write(str(result))

    print("Результат записан в result.txt")


def main():
    try:
        with open("input.txt", "r", encoding="utf-8") as f:
            mode = f.readline().strip()

        if mode == "1":
            case_file()
        else:
            case_console()

    except FileNotFoundError:
        case_console()
    except Exception as e:
        print("Ошибка:", e)


if __name__ == "__main__":
    main()