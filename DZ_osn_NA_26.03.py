import inspect
from board import Board #из файла board.py импортнули мы класс Board
b1 = Board(3, 3)
b2 = Board(8, 8)
b3 = Board(6, 10)
#КОД КЛАССА С ПОМОЩЬЮ ИНСПЕКТА
print(inspect.getsource(Board)) #показывает исходный код объекта
#ИНФА ПРО ОБЪЕКТЫ
print(b1)
print(b2)
print(b3)
print(type(b1)) #просто тип объекта
print(inspect.getmodule(b1)) #в каком модуле был определен, будет боард ща