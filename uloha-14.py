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
