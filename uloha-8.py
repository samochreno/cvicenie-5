def zostupne(zoznam):
    for i in range(1, len(zoznam)):
        if zoznam[i] > zoznam[i - 1]:
            return False
    return True
