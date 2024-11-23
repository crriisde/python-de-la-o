print(" ")
print(" Cristian David Salas De La O 3-W")
print(" ")

def superposicion(lista1, lista2):
    for elemento1 in lista1:
        for elemento2 in lista2:
            if elemento1 == elemento2:
                return True
    return False

print(superposicion([1, 2, 3], [4, 2, 5]))  # Devuelve True
print(superposicion([1, 2, 3], [4, 5, 6]))  # Devuelve False
