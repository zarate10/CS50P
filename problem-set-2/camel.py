"""
En algunos idiomas, es común usar mayúsculas y minúsculas (también conocidas como "mayúsculas mixtas") para los nombres de las variables cuando esos nombres comprenden varias palabras, por lo que la primera letra de la primera palabra está en minúsculas pero la primera letra de cada palabra subsiguiente está en mayúsculas. . Por ejemplo, mientras que una variable para el nombre de un usuario podría llamarse name, una variable para el nombre de un usuario podría llamarse firstName, y una variable para el nombre preferido de un usuario (por ejemplo, apodo) podría llamarse preferredFirstName.

Python, por el contrario, recomienda caso de serpiente , en el que las palabras están separadas por guiones bajos ( _), con todas las letras en minúsculas. Por ejemplo, esas mismas variables se llamarían name, first_name, y preferred_first_name, respectivamente, en Python.

En un archivo llamado camel.py, implemente un programa que solicite al usuario el nombre de una variable en mayúsculas y minúsculas y arroje el nombre correspondiente en mayúsculas y minúsculas. Suponga que la entrada del usuario estará en caso de camello. 
"""
def add_word(str, arr, index_start, index_stop):

    wordAux = []

    for i in range(index_start, index_stop):
        wordAux.append(str[i])

    word = ''.join(wordAux)
    #print(word)
    arr.append(word)

def detect_words(str):

    words = []
    pos = []

    for i in range(len(str)):

        if str[i] == str[i].upper():
            pos.append(i)

    add_word(str, words, 0, pos[0])

    if not pos:
        return str
    else:
        if len(pos) <= 1:
            add_word(str, words, pos[0], len(str))
        else:
            for i in range(len(pos) - 1):
                    add_word(str, words, pos[i], pos[i + 1])
                    if i == len(pos) - 2:
                        add_word(str, words, pos[len(pos) - 1], len(str))
                #print(pos[len(pos) - 1])

        return words

def to_snake():
    camel_user = input('camelCase: ')
    words = detect_words(camel_user)

    print('_'.join(words).lower())

to_snake()