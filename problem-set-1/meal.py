"""
En meal.py, implemente un programa que le solicite al usuario una hora y le indique si es la hora del desayuno, la hora del almuerzo o la hora de la cena.  Si no es hora de comer, no envíes nada.  Suponga que la entrada del usuario se formateará en formato de 24 horas como #:## o ##:##.  Y suponga que el rango de tiempo de cada comida es inclusivo.  Por ejemplo, ya sean las 7:00, las 7:01, las 7:59 o las 8:00, o en cualquier momento intermedio, es hora de desayunar.
"""
def meal():
    time = input('What time is it?: ')
    hour, min = time.split(':')

    hour = int(hour)
    min = int(min)

    if (hour >= 0 and hour <= 23) and (min >= 0 and min <= 59):

        if (hour == 7 and min >= 0 and min <= 59) or (hour == 8 and min == 0):
            print('breakfast time')
        elif (hour == 12 and min >= 0 and min <= 59) or (hour == 13 and min == 0):
            print('lunch time')
        elif (hour == 18 and min >= 0 and min <= 59) or (hour == 19 and min == 0):
            print('dinner time')

meal()