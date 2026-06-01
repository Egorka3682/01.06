indent_level = 0

def printIn(s):
    global indent_level
    print("    " * indent_level + s)
    indent_level += 1

def printOut(s):
    global indent_level
    indent_level -= 1
    print("    " * indent_level + s)

def fib(n):
    printIn(f"fib({n})")
    if n == 0:
        res = 0
        printOut(str(res))
        return res
    elif n == 1 or n == -1:
        res = 1
        printOut(str(res))
        return res
    elif n > 0:
        res = fib(n - 1) + fib(n - 2)
        printOut(str(res))
        return res
    else:
        res = fib(-n) * ((-1) ** (n + 1))
        printOut(str(res))
        return res

fib(5)