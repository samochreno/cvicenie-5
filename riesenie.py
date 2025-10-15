# 6. cvicenie
# student: Samuel Chreno
# datum: 15.10.2025

def fibonacci(zoznam, n):
    for _ in range(n):
        dalsi = zoznam[-1] + zoznam[-2]
        zoznam.append(dalsi)

def cifry(cislo, sustava=10):
    if cislo == 0:
        return [0]
    vysledok = []
    while cislo > 0:
        zvysok = cislo % sustava
        vysledok.append(zvysok)
        cislo = cislo // sustava
    vysledok.reverse()
    return vysledok

def zostupne(zoznam):
    for i in range(1, len(zoznam)):
        if zoznam[i] > zoznam[i - 1]:
            return False
    return True

def postupnost(start, koniec, krok=1):
    vysledok = []
    if krok == 0:
        return vysledok
    hodnota = start
    if krok > 0:
        if hodnota >= koniec:
            return vysledok
        while hodnota < koniec:
            vysledok.append(hodnota)
            hodnota += krok
    else:
        if hodnota <= koniec:
            return vysledok
        while hodnota > koniec:
            vysledok.append(hodnota)
            hodnota += krok
    return vysledok

def sucet(zoznam1, zoznam2):
    vysledok = []
    dlzka1 = len(zoznam1)
    dlzka2 = len(zoznam2)
    minimum = dlzka1
    if dlzka2 < minimum:
        minimum = dlzka2
    for i in range(minimum):
        vysledok.append(zoznam1[i] + zoznam2[i])
    if dlzka1 > minimum:
        for i in range(minimum, dlzka1):
            vysledok.append(zoznam1[i])
    else:
        for i in range(minimum, dlzka2):
            vysledok.append(zoznam2[i])
    return vysledok

def rozklad(cislo):
    vysledok = []
    if cislo < 2:
        return tuple(vysledok)
    delitel = 2
    while cislo > 1:
        while cislo % delitel == 0:
            vysledok.append(delitel)
            cislo = cislo // delitel
        delitel += 1
    return tuple(vysledok)

def vsetky_rozne(postupnost):
    pomocny = list(postupnost)
    pomocny.sort()
    for i in range(1, len(pomocny)):
        if pomocny[i] == pomocny[i - 1]:
            return False
    return True

def enum(postupnost):
    vysledok = []
    index = 0
    for prvok in postupnost:
        vysledok.append((index, prvok))
        index += 1
    return tuple(vysledok)

def moj_zip(post1, post2):
    zoznam1 = list(post1)
    zoznam2 = list(post2)
    dlzka1 = len(zoznam1)
    dlzka2 = len(zoznam2)
    minimum = dlzka1
    if dlzka2 < minimum:
        minimum = dlzka2
    vysledok = []
    for i in range(minimum):
        vysledok.append((zoznam1[i], zoznam2[i]))
    return vysledok

def do_dvojic(postupnost):
    zoznam = list(postupnost)
    vysledok = []
    for i in range(0, len(zoznam), 2):
        vysledok.append((zoznam[i], zoznam[i + 1]))
    return vysledok
