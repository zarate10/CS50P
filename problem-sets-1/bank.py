"""
En un archivo llamado bank.py, implemente un programa que solicite al usuario un saludo.  Si el saludo comienza con "hola", genera $0.  Si el saludo comienza con una "h" (pero no "hola"), genere $20.  De lo contrario, genera $100.  Ignore cualquier espacio en blanco inicial en el saludo del usuario y trate el saludo del usuario sin distinción entre mayúsculas y minúsculas.
"""
def bank_greeting():

    user_greeting = input('Greeting: ').lower()

    if user_greeting.find('hello') != -1:
        return '$0'
    elif user_greeting[0] == 'h':
        return '$20'
    else:
        return '$100'

print(bank_greeting())