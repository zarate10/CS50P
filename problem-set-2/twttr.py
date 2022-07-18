"""
Al enviar mensajes de texto o twittear, no es raro acortar las palabras para ahorrar tiempo o espacio, por ejemplo, omitiendo las vocales, al igual que Twitter originalmente se llamaba twttr.  En un archivo llamado twttr.py, implemente un programa que solicite al usuario una cadena de texto y luego emita ese mismo texto pero con todas las vocales (A, E, I, O y U) omitidas, ya sea que se ingresen en mayúsculas o minúsculas. .
"""
def twttr():
    vowels = ['a', 'e', 'i', 'o', 'u']
    user_txt = input('Input: ')

    nw_wrd = []

    for i in range(len(user_txt)):

        count = 0

        for j in range(len(vowels)):
            
            if user_txt[i] != vowels[j]: 
                count += 1

        if count == len(vowels):
            nw_wrd.append(user_txt[i])

    print(''.join(nw_wrd))

twttr()

