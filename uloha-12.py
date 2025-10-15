def vsetky_rozne(postupnost):
    pomocny = list(postupnost)
    pomocny.sort()
    for i in range(1, len(pomocny)):
        if pomocny[i] == pomocny[i - 1]:
            return False
    return True
