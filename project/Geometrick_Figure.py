import os
from itertools import combinations


class Point:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __str__(self):
        return f"({self.x}, {self.y})"


class Polygon:
    def __init__(self, name, points):
        self.name = name
        self.points = points

    def sides(self):
        result = []
        n = len(self.points)

        for i in range(n):
            p1 = self.points[i]
            p2 = self.points[(i + 1) % n]
            result.append((p1, p2))

        return result

    def contains_point(self, point):
        count = 0
        n = len(self.points)

        for i in range(n):
            a = self.points[i]
            b = self.points[(i + 1) % n]

            if point_on_segment(point, a, b):
                return True

            if (a.y > point.y) != (b.y > point.y):
                x_cross = (b.x - a.x) * (point.y - a.y) / (b.y - a.y) + a.x

                if point.x < x_cross:
                    count += 1

        return count % 2 == 1

    def intersects(self, other):
        for a1, a2 in self.sides():
            for b1, b2 in other.sides():
                if segments_intersect(a1, a2, b1, b2):
                    return True

        if self.contains_point(other.points[0]):
            return True

        if other.contains_point(self.points[0]):
            return True

        return False

    def __str__(self):
        return self.name


def orientation(a, b, c):
    value = (b.y - a.y) * (c.x - b.x) - (b.x - a.x) * (c.y - b.y)

    if abs(value) < 0.000001:
        return 0

    if value > 0:
        return 1

    return 2


def point_on_segment(p, a, b):
    if orientation(a, p, b) != 0:
        return False

    return min(a.x, b.x) <= p.x <= max(a.x, b.x) and min(a.y, b.y) <= p.y <= max(a.y, b.y)


def segments_intersect(a1, a2, b1, b2):
    o1 = orientation(a1, a2, b1)
    o2 = orientation(a1, a2, b2)
    o3 = orientation(b1, b2, a1)
    o4 = orientation(b1, b2, a2)

    if o1 != o2 and o3 != o4:
        return True

    if o1 == 0 and point_on_segment(b1, a1, a2):
        return True

    if o2 == 0 and point_on_segment(b2, a1, a2):
        return True

    if o3 == 0 and point_on_segment(a1, b1, b2):
        return True

    if o4 == 0 and point_on_segment(a2, b1, b2):
        return True

    return False


def line_intersection(a1, a2, b1, b2):
    x1, y1 = a1.x, a1.y
    x2, y2 = a2.x, a2.y
    x3, y3 = b1.x, b1.y
    x4, y4 = b2.x, b2.y

    d = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)

    if abs(d) < 0.000001:
        return None

    px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / d
    py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / d

    p = Point(px, py)

    if point_on_segment(p, a1, a2) and point_on_segment(p, b1, b2):
        return p

    return None


def load_polygons(folder):
    polygons = []

    for filename in os.listdir(folder):
        path = os.path.join(folder, filename)

        if os.path.isfile(path):
            with open(path, "r", encoding="utf-8") as file:
                name = file.readline().strip()
                n = int(file.readline())

                points = []

                for i in range(n):
                    x, y = file.readline().split()
                    points.append(Point(x, y))

                polygons.append(Polygon(name, points))

    return polygons


def all_pairwise_intersect(polygons):
    for p1, p2 in combinations(polygons, 2):
        if not p1.intersects(p2):
            return False

    return True


def find_common_point(polygons):
    candidates = []

    for polygon in polygons:
        for point in polygon.points:
            candidates.append(point)

    for p1, p2 in combinations(polygons, 2):
        for a1, a2 in p1.sides():
            for b1, b2 in p2.sides():
                point = line_intersection(a1, a2, b1, b2)

                if point is not None:
                    candidates.append(point)

    for point in candidates:
        ok = True

        for polygon in polygons:
            if not polygon.contains_point(point):
                ok = False
                break

        if ok:
            return point

    return None


def find_max_subset(polygons):
    best_subset = []

    for size in range(1, len(polygons) + 1):
        for subset in combinations(polygons, size):
            subset = list(subset)

            if all_pairwise_intersect(subset):
                point = find_common_point(subset)

                if point is not None:
                    best_subset = subset

    return best_subset


def show_polygons(polygons):
    print("Загруженные многоугольники:")

    for polygon in polygons:
        print("-", polygon.name)


def menu():
    polygons = load_polygons("polygons")

    while True:
        print("\nМеню:")
        print("1. Показать все многоугольники")
        print("2. Найти подмножество попарно пересекающихся многоугольников")
        print("3. Найти общую точку для всех многоугольников")
        print("4. Найти максимальное подмножество")
        print("0. Выход")

        choice = input("Выберите пункт: ")

        if choice == "1":
            show_polygons(polygons)

        elif choice == "2":
            if all_pairwise_intersect(polygons):
                print("Все многоугольники попарно пересекаются.")
            else:
                print("Не все многоугольники попарно пересекаются.")

        elif choice == "3":
            point = find_common_point(polygons)

            if point is not None:
                print("Общая точка:", point)
            else:
                print("Общая точка не найдена.")

        elif choice == "4":
            subset = find_max_subset(polygons)

            if len(subset) > 0:
                print("Максимальное подмножество:")
                for polygon in subset:
                    print("-", polygon.name)

                point = find_common_point(subset)
                print("Общая точка:", point)
            else:
                print("Подмножество не найдено.")

        elif choice == "0":
            break

        else:
            print("Неверный пункт меню.")


menu()