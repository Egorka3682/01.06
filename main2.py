def func(*n):
    try:
        rez =1
        for i in n:
            if type(n) not in (float, int):
                raise ValueError
            rez *= n
        return rez
    except ValueError:
        return "аргумент не число"


# def multiply(a, b=None, c=None):
#     result = a
#     if b is not None:
#         result *= b
#     if c is not None:
#         result *= c
#     return result
#
# print(f"multiply(5) = {multiply(5)}")  # 5
# print(f"multiply(-2, 5) = {multiply(-2, 5)}")  # -10
# print(f"multiply(-1, 2, -3) = {multiply(-1, 2, -3)}")  # 6
#
#
#
# a = [2, 5, 7, 3, 8]
# result = [value * index for index, value in enumerate(a)]
# print(result)
