def func(*functions):
    st={}
    for fnc in functions:
        dc=fnc.__doc__
        if dc and dc.strip():
            f_word=dc.strip().split()[0]
            st[f_word]=fnc
        else:
            continue
    return st

def repl(func_dt):
    while True:
        cmd = input("- ").strip()
        if cmd == "exit":
            break
        if not cmd:
            continue
        
        parts = cmd.split()
        key = parts[0]
        args = parts[1:]
        
        if key not in func_dt:
            print("Что за функция")
            continue
        
        kwargs = {}
        new_args = []
        for a in args:
            if '=' in a:
                k,v = a.split('=',1)
                try:
                    kwargs[k] = int(v) if v.isdigit() else float(v) if '.' in v else v
                except:
                    kwargs[k] = v
            else:
                try:
                    new_args.append(int(a) if a.isdigit() else float(a) if '.' in a else a)
                except:
                    new_args.append(a)
        
        try:
            print(func_dt[key](*new_args, **kwargs))
        except Exception as e:
            print(f"Ошибка {e}")


def slime(*a):
    '''Склеивание строк'''
    b=[]
    for x in a:
        b.append(str(x))
    return ''.join(b)

def add(a,b):
    '''Сложение чисел'''
    return a+b

def minus(a,b):
    '''Вычитание чисел'''
    return a-b

def multiply(a,b):
    '''Умножение чисел'''
    return a*b

def delit(a,b):
    '''Деление чисел'''
    return a/b

def brosit(rasstoyanie):
    '''БРОСИТЬ'''
    return f"Предмет брошен на расстояние {rasstoyanie}"


sii=func(add,minus,multiply,delit,slime,brosit)
repl(sii)