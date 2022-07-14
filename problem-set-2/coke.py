"""
Supongamos que una máquina vende botellas de Coca-Cola (Coca-Cola) a 50 centavos y solo acepta monedas en estas denominaciones: 25 centavos, 10 centavos y 5 centavos.

En un archivo llamado coke.py, implemente un programa que solicite al usuario que inserte una moneda, una a la vez, informando cada vez al usuario de la cantidad adeudada.  Una vez que el usuario haya ingresado al menos 50 centavos, indique cuántos centavos en cambio se le deben al usuario.  Suponga que el usuario solo ingresará números enteros e ignorará cualquier número entero que no sea una denominación aceptada.
"""
def coke():
    amount_due = 50
    while amount_due > 0:
        coin = int(input('Insert Coin: '))

        if (coin == 25 or coin == 10 or coin == 5) and (amount_due - coin >= 0):
            amount_due -= coin

        print('Amount Due: ', amount_due)

coke()