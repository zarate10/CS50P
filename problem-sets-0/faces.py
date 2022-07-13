"""
En un archivo llamado faces.py, implemente una función llamada convert que acepte una str como entrada y devuelva esa misma entrada con cualquier :) convertido a 🙂 (también conocido como una cara ligeramente sonriente) y cualquier :( convertido a 🙁 (también conocido como una cara con el ceño ligeramente fruncido). El resto del texto debe devolverse sin cambios.

Luego, en ese mismo archivo, implemente una función llamada main que solicite al usuario una entrada, llame a convert en esa entrada e imprima el resultado.  Le invitamos, pero no es obligatorio, a solicitar al usuario explícitamente, pasando una cadena propia como argumento para la entrada.  Asegúrese de llamar a main en la parte inferior de su archivo.
"""

def convert(word):
    if word == ":)":
        return "🙂"
    else:
        return "🙁"

def main():
    text = input().split()

    for word in text:
        if word == ":)" or word == ":(":
            ind = text.index(word)
            text[ind] = convert(word)

    for word in text:
        print(word, end=" ")


main()