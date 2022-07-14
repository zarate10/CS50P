"""
En un archivo llamado interpreter.py, implemente un programa que solicite al usuario una expresión aritmética y luego calcule y emita el resultado como un valor de punto flotante con formato de un lugar decimal.  Suponga que la entrada del usuario se formateará como xyz, con un espacio entre x e y y un espacio entre y y z, donde:

- x es un flotante
- y es +, -, * o /
- z es un flotante
"""
def interpreter():
    expression = input('Expression: ')
    x, y, z = expression.split(' ')

    x = float(x)
    z = float(z)

    if y == '+':
        print(x + z)
    elif y == '-':
        print(x - z)
    elif y == '*':
        print(x * z)
    elif y == '/':
        print(x / z)

interpreter()