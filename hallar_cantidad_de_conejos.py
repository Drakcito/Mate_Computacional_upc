def calcular_conejos(n, c0, c1):
    if n == 0:
        return c0
    elif n == 1:
        return c1
    else:
        return calcular_conejos(n-1, c0, c1) + (3/4) * (calcular_conejos(n-1, c0, c1) - calcular_conejos(n-2, c0, c1)) + 25 #Recursiva

c0 = 40
c1 = 50

n = 2
while calcular_conejos(n, c0, c1) < 608:
    cantidad_conejos = calcular_conejos(n, c0, c1)
    if cantidad_conejos >= 607:
        print(f"Después de {n} meses, la cantidad de conejos es aproximadamente {cantidad_conejos}")
    elif cantidad_conejos < 607:
        print(f"C{n} =  {cantidad_conejos}")

    n += 1
