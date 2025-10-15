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
