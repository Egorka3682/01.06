with open("C:\\Users\\vikto\\Desktop\\Новый текстовый документ.txt", "r", encoding='utf-8') as f:
    rez=f.readlines()
    print(rez)
    d = dict
    t = input("товар: ")
    for i in rez:
        if t == i.split(":")[0]:
            print(i.split(":")[1])
        d[i.split(":")[0]] = i.split(":")[1]
print(d)
for i in range(3):
    tov = input("товар")
    cena = input("цена") + "\n"
    d[tov] = cena
print(d)
with open("C:\\Users\\vikto\\Desktop\\Новый текстовый документ.txt", "r", encoding='utf-8') as f:
    for i, j in d.items():
        f1.write()