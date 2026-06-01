
# ТОД 7 — все номера + задание 9, вариант 9

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns

# ---------- загрузка данных ----------
average_ratings = np.load('/mnt/data/average_ratings.npy')
visitors = np.load('/mnt/data/visitors.npy')
recipes = pd.read_csv('/mnt/data/recipes_sample (2).csv')

# Для заданий 6 и 8 нужен файл reviews из ЛР2.
# Если он у тебя есть, просто раскомментируй следующую строку:
# reviews = pd.read_csv('reviews_sample.csv')


# =========================================================
# 1
# =========================================================
recipe_names = [
    'waffle iron french toast',
    'zwetschgenkuchen bavarian plum cake',
    'lime tea'
]

days = np.arange(average_ratings.shape[1])

plt.figure(figsize=(12, 6))
for i in range(3):
    plt.plot(days, average_ratings[i], label=recipe_names[i])

plt.xlabel('Номер дня')
plt.ylabel('Средний рейтинг')
plt.title('Изменение среднего рейтинга трех рецептов')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()


# =========================================================
# 2
# =========================================================
dates = pd.date_range(start='2019-01-01', end='2021-12-30', freq='D')

fig, ax = plt.subplots(figsize=(14, 6))

for i in range(3):
    ax.plot(dates, average_ratings[i], label=recipe_names[i])

ax.set_xlabel('Дата')
ax.set_ylabel('Средний рейтинг')
ax.set_title('Изменение среднего рейтинга трех рецептов')
ax.legend()

ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())

ax.grid(True, which='major', alpha=0.6)
ax.grid(True, which='minor', alpha=0.3, linestyle=':')

plt.tight_layout()
plt.show()


# =========================================================
# 3
# =========================================================
fig, axes = plt.subplots(3, 1, figsize=(14, 10), sharex=True)

for i in range(3):
    axes[i].plot(dates, average_ratings[i], label=recipe_names[i])
    axes[i].set_ylabel('Средний рейтинг')
    axes[i].legend(loc='best')
    axes[i].grid(True, which='major', alpha=0.6)
    axes[i].grid(True, which='minor', alpha=0.3, linestyle=':')

axes[-1].set_xlabel('Дата')
axes[0].set_title('Изменение среднего рейтинга трех рецептов')

axes[-1].xaxis.set_major_locator(mdates.YearLocator())
axes[-1].xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
axes[-1].xaxis.set_minor_locator(mdates.MonthLocator())

plt.tight_layout()
plt.show()


# =========================================================
# 4
# =========================================================
days_vis = np.arange(1, len(visitors) + 1)

fig, axes = plt.subplots(1, 2, figsize=(16, 6))

for ax in axes:
    ax.plot(days_vis, visitors)
    ax.axhline(y=100, color='red')
    ax.text(days_vis[len(days_vis)//2], visitors.max() * 0.92, r'$y(x)=\lambda e^{-\lambda x}$',
            ha='center')
    ax.text(days_vis[len(days_vis)//2], 120, r'$y(x)=100$', color='red', ha='center')
    ax.set_xlabel('Количество дней с момента акции')
    ax.set_ylabel('Число посетителей')

axes[0].set_title('Линейный масштаб')
axes[1].set_title('Логарифмический масштаб')
axes[1].set_yscale('log')

fig.suptitle('Изменение количества пользователей в линейном и логарифмическом масштабе')
plt.tight_layout()
plt.show()


# =========================================================
# 5
# =========================================================
recipes_5 = recipes.copy()

recipes_5['group'] = pd.cut(
    recipes_5['minutes'],
    bins=[-np.inf, 5, 50, np.inf],
    right=False,
    labels=['Короткие', 'Средние', 'Длинные']
)

group_stats = recipes_5.groupby('group', observed=True).agg(
    avg_steps=('n_steps', 'mean'),
    group_size=('id', 'count')
).reindex(['Короткие', 'Средние', 'Длинные'])

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

group_stats['avg_steps'].plot(kind='bar', ax=axes[0])
axes[0].set_xlabel('Группа рецептов')
axes[0].set_ylabel('Средняя длительность')
axes[0].set_title('Среднее количество шагов')

group_stats['group_size'].plot(kind='pie', ax=axes[1], autopct='%1.1f%%')
axes[1].set_title('Размеры групп рецептов')
axes[1].set_ylabel('')

plt.tight_layout()
plt.show()


# =========================================================
# 6
# =========================================================
# Нужна таблица reviews с колонками date и rating.
# Пример рабочего кода:

"""
reviews['date'] = pd.to_datetime(reviews['date'])

reviews_2008 = reviews[reviews['date'].dt.year == 2008]
reviews_2009 = reviews[reviews['date'].dt.year == 2009]

fig, axes = plt.subplots(1, 2, figsize=(14, 5), sharey=True)

reviews_2008['rating'].plot.hist(ax=axes[0], bins=20)
axes[0].set_title('2008')

reviews_2009['rating'].plot.hist(ax=axes[1], bins=20)
axes[1].set_title('2009')
axes[1].set_ylabel('')

fig.suptitle('Гистограммы рейтинга отзывов в 2008 и 2009 годах')
plt.tight_layout()
plt.show()
"""


# =========================================================
# 7
# =========================================================
recipes_7 = recipes.copy()

recipes_7['group'] = pd.cut(
    recipes_7['minutes'],
    bins=[-np.inf, 5, 50, np.inf],
    right=False,
    labels=['Короткие', 'Средние', 'Длинные']
)

recipes_7 = recipes_7.dropna(subset=['n_steps', 'n_ingredients', 'group'])

plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=recipes_7,
    x='n_steps',
    y='n_ingredients',
    hue='group'
)

plt.title('Диаграмма рассеяния n_steps и n_ingredients')
plt.xlabel('n_steps')
plt.ylabel('n_ingredients')
plt.grid(True, alpha=0.3)
plt.show()

# Текстовый вывод:
print('Визуально строгой линейной зависимости не наблюдается. '
      'Есть общий рост: при увеличении числа шагов обычно растет и число ингредиентов, '
      'но точки расположены довольно рассеянно.')


# =========================================================
# 8
# =========================================================
# Нужна таблица reviews.
# Пример рабочего кода:

"""
merged = recipes.merge(reviews, left_on='id', right_on='recipe_id')

corr = merged[['minutes', 'n_steps', 'n_ingredients', 'rating']].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap='YlOrRd')
plt.title('Корреляционная матрица числовых столбцов таблиц recipes и reviews')
plt.show()
"""


# =========================================================
# 9 — вариант 9
# =========================================================
x = np.linspace(0, 2 * np.pi, 95)

y1 = np.cos(x)
y2 = np.cos(3 * x)
y3 = y1 + y2

# HEX-цвета:
# розовый, хаки, синий
c1 = '#FFC0CB'
c2 = '#BDB76B'
c3 = '#0000FF'

plt.figure(figsize=(12, 6))

plt.plot(x, y1, linestyle='-.', linewidth=2, color=c1, label='y1 = cos(x)')
plt.plot(x, y2, linestyle='-', linewidth=2, color=c2, label='y2 = cos(3x)')
plt.scatter(x, y3, marker='h', s=45, color=c3, label='y3 = y1 + y2')

plt.step(x, y3, where='mid', color=c3, linestyle=':', linewidth=1.5, alpha=0.9, label='Доп. график y3 (step)')

plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.title('Вариант 9: графики функций y1, y2 и y3')

plt.xticks(np.arange(0, 2 * np.pi + 0.35, 0.35))
plt.yticks(np.arange(-2, 2.5, 0.35))

plt.grid(True, alpha=0.4, linestyle='--')
plt.legend(loc='center')

plt.tight_layout()
plt.show()

# Краткие ответы:
print('1) Чем больше точек в linspace, тем более гладким и точным выглядит график. '
      'Если точек мало, линия кажется грубее и может хуже передавать форму функции.')

print('2) plot соединяет точки линиями и подходит для непрерывных функций. '
      'scatter показывает отдельные точки без соединения линиями.')

print('3) Для y3 выбран scatter, потому что по условию варианта нужно показать эту функцию точечной диаграммой. '
      'Так также проще визуально отделить y3 от двух линейных графиков.')
