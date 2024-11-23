print(" ")
print(" Cristian David Salas De La O 3-W")
print(" ")

def es_palindromo(palabra):
    return palabra == palabra[::-1]

print(es_palindromo("radar"))  # Devuelve True
print(es_palindromo("hola"))   # Devuelve False
