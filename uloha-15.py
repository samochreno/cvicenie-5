def do_dvojic(postupnost):
    zoznam = list(postupnost)
    vysledok = []
    for i in range(0, len(zoznam), 2):
        vysledok.append((zoznam[i], zoznam[i + 1]))
    return vysledok
