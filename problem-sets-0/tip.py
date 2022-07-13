"""
En los Estados Unidos, se acostumbra dejar una propina a su mesero después de cenar en un restaurante, generalmente una cantidad igual al 15% o más del costo de su comida.  Sin embargo, no se preocupe, ¡hemos escrito una calculadora de propinas para usted, a continuación!

Bueno, hemos escrito la mayor parte de una calculadora de propinas para ti.  Desafortunadamente, no tuvimos tiempo de implementar dos funciones:

- dollar_to_float, que debe aceptar una cadena como entrada (formateada como $##.##, donde cada # es un dígito decimal), eliminar el $ inicial y devolver la cantidad como un valor flotante.  Por ejemplo, dado $50,00 como entrada, debería devolver 50,0.
- percent_to_float, que debería aceptar un str como entrada (formateado como ##%, donde cada # es un dígito decimal), eliminar el % final y devolver el porcentaje como un flotante.  Por ejemplo, dado el 15 % como entrada, debería devolver 0,15.
"""
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    cost = d.replace ("$", "")
    return float(cost)

def percent_to_float(p):
    percent = p.replace ("%", "")
    return float(percent) / 100

main()