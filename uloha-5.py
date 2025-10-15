def fibonacci(zoznam, n):
    for _ in range(n):
        dalsi = zoznam[-1] + zoznam[-2]
        zoznam.append(dalsi)
