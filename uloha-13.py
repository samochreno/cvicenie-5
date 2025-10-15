def enum(postupnost):
    vysledok = []
    index = 0
    for prvok in postupnost:
        vysledok.append((index, prvok))
        index += 1
    return tuple(vysledok)
