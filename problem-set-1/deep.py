"""
En deep.py, implemente un programa que solicite al usuario la respuesta a la Gran pregunta de la vida, el universo y todo, mostrando Sí si el usuario ingresa 42 o (sin distinción entre mayúsculas y minúsculas) cuarenta y dos o cuarenta y dos.  De lo contrario, salida No.
"""
def deep():

    answers = ['42', 'forty two', 'forty-two']
    user_ans = input('What is the Answer to the Great Question of Life, the Universe, and Everything?: ').lower().strip()

    found = 'No'

    for i in range(len(answers)):
        if answers[i] == user_ans:
            found = 'Yes'

    return found


print(deep())