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
