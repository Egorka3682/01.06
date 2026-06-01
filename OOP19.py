#КЛАСС ДОМА, ДА
class House:
    def __init__(self, floor, kolpod, rayon, sroks, srokpo):
        self.floor = floor
        self.kolpod = kolpod
        self.rayon = rayon
        self.workers = []
        self.sroks = sroks
        self.srokpo = srokpo
    #ЭТА ШТУКА ВЕРНЕТ ГОДЫ НАЧАЛА И КОНЦА СТРОИТЕЛЬСТВА ДОМА
    def get_years(self):
        return set([self.sroks.split('.')[-1], self.srokpo.split('.')[-1]])
#КЛАСС РАБОТНИКА
class Workerss:
    def __init__(self, namecomp, kvalif, nameworker):
        self.namecomp = namecomp
        self.kvalif = kvalif
        self.nameworker = nameworker

w1 = Workerss('СтройИнвест', 'каменщик', 'Иван')
w2 = Workerss('СтройИнвест', 'штукатур', 'Петр')
w3 = Workerss('МегаСтрой', 'плиточник', 'Сидор')
w4 = Workerss('МегаСтрой', 'каменщик', 'Алексей')
h1 = House(9, 4, 'Центр', '01.03.2022', '01.12.2022')
h1.workers = [w1, w2] #НАД ДОМОМ H1 РАБОТАЮТ РАБОТНИКИ W1 И W2 ТИП
h2 = House(5, 2, 'Север', '01.05.2022', '01.10.2023')
h2.workers = [w1, w3]
h3 = House(16, 6, 'Юг', '01.06.2023', '01.11.2023')
h3.workers = [w4, w2]
houses = [h1, h2, h3]
year2022 = '2022' #ДОПУСТИМ НАС ИНТЕРЕСУЕТ 2022 ГОД
#ПОДСЧИТЫВАЕМ КОРОЧЕ СКОЛЬКО ДОМОВ КАЖДЫЙ РАБОЧИЙ СТРОИЛ В 2022 ГОДУ
for worker in [w1, w2, w3, w4]:
    count = 0
    for house in houses:
        # ЕСЛИ РАБОЧИЙ ЕСТЬ В СПИСКЕ РАБОЧИХ У ДОМА И ГОД СТРОИТЕЛЬСТВА ДОМА ВКЛЮЧАЕТ 2022
        if worker in house.workers and year2022 in house.get_years():
            count += 1
    print(f'{worker.kvalif} ({worker.namecomp}) строит {count} дома в {year2022}')