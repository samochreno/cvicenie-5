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
