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
