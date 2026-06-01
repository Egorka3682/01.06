def read_preferences(filename):
    """Чтение списков предпочтений из файла"""
    preferences = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                # Разделяем строку по запятым
                elements = line.split(',')
                prefs = []
                for elem in elements:
                    # Пробуем преобразовать в int, если не получается - оставляем str
                    try:
                        # Пробуем преобразовать в int
                        num = elem
                        # Проверяем, что это действительно целое число без лишних символов
                        if (num) == elem:  # проверка, что не было пробелов или других символов
                            prefs.append(num)
                        else:
                            prefs.append(elem)
                    except ValueError:
                        prefs.append(elem)
                preferences.append(prefs)
    return preferences


def get_all_options(preferences):
    """Получить все уникальные варианты голосования"""
    options = set()
    for pref in preferences:
        for option in pref:
            options.add(option)
    # Сортируем как строки для лексикографического порядка
    return sorted(options, key=lambda x: str(x))


def count_first_place_votes(preferences, remaining_options):
    """Подсчет голосов за первые места"""
    vote_counts = {option: 0 for option in remaining_options}

    for pref in preferences:
        if pref:  # если список предпочтений не пустой
            first_choice = pref[0]
            if first_choice in remaining_options:
                vote_counts[first_choice] += 1

    return vote_counts


def find_winners(vote_counts):
    """Найти варианты с наибольшим количеством голосов"""
    if not vote_counts:
        return []

    max_votes = max(vote_counts.values())
    winners = [option for option, votes in vote_counts.items() if votes == max_votes]
    # Сортируем как строки для лексикографического порядка
    return sorted(winners, key=lambda x: str(x))


def remove_options_from_preferences(preferences, options_to_remove):
    """Удалить указанные варианты из всех списков предпочтений"""
    new_preferences = []
    for pref in preferences:
        new_pref = [option for option in pref if option not in options_to_remove]
        new_preferences.append(new_pref)
    return new_preferences


def modified_plurality_method(preferences):
    """Основной алгоритм модифицированного метода относительного большинства"""
    all_options = get_all_options(preferences)
    remaining_options = set(all_options)
    ranking = []

    current_preferences = preferences.copy()

    while remaining_options:
        # Подсчитываем голоса за первые места
        vote_counts = count_first_place_votes(current_preferences, remaining_options)

        # Если нет голосов за оставшиеся варианты, все оставшиеся занимают текущее место
        if not any(vote_counts.values()):
            winners = sorted(remaining_options, key=lambda x: str(x))  # Лексикографическая сортировка
        else:
            winners = find_winners(vote_counts)

        # Добавляем победителей в рейтинг
        if len(winners) == 1:
            ranking.append(winners[0])
        else:
            ranking.append(winners)

        # Удаляем победителей из оставшихся вариантов
        remaining_options -= set(winners)

        # Удаляем победителей из всех списков предпочтений
        current_preferences = remove_options_from_preferences(current_preferences, winners)

    return ranking


def format_ranking(ranking):
    """Форматирование рейтинга в требуемый вид"""
    result_parts = []
    for item in ranking:
        if isinstance(item, list):
            # Несколько вариантов на одном месте
            items_formatted = []
            for x in item:
                if isinstance(x, str):
                    items_formatted.append(x)
                else:
                    items_formatted.append(str(x))
            result_parts.append("[" + ",".join(items_formatted) + "]")
        else:
            # Один вариант
            if isinstance(item, str):
                result_parts.append(item)
            else:
                result_parts.append(str(item))

    return ",".join(result_parts)


def main():
    # Читаем предпочтения из файла
    try:
        preferences = read_preferences("input.txt")

        # Проверка на пустые предпочтения
        if not preferences:
            print("Файл input.txt пуст или не содержит данных!")
            return

    except FileNotFoundError:
        print("Файл input.txt не найден!")
        return
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return

    # Применяем модифицированный метод относительного большинства
    ranking = modified_plurality_method(preferences)

    # Форматируем результат
    result = format_ranking(ranking)

    # Записываем результат в файл
    try:
        with open("result.txt", "w") as file:
            file.write(result)
        print("Результат успешно записан в файл result.txt")
    except Exception as e:
        print(f"Ошибка при записи файла: {e}")


# Запускаем программу
if __name__ == "__main__":
    main()