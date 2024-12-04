def calcularCuota(monto,interes,meses):
    interesmensual=interes/12
    inter=interesmensual/100
    cuotamensual=(monto*inter)/(1-(1+inter)**(-meses))
    return cuotamensual


import datetime
def calcularEdad (fecha):
    añoactual = datetime.datetime.now().year 
    if fecha >= 0 and fecha <= añoactual:
        edad = añoactual - fecha
        return edad
    else:
        return -1


def determinarResultadosIMC(imc):
    if 0 <= imc < 16:
        return "Delgadez severa"
    elif 16 <= imc < 17:
        return "Delgadez moderada"
    elif 17 <= imc < 18.5:
        return "Delgadez leve"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    elif 30 <= imc < 35:
        return "Obesidad Grado 1"
    elif 35 <= imc < 40:
        return "Obesidad Grado 2"
    elif imc >= 40:
        return "Obesidad Grado 3"
    else:
        return "IMC fuera de rango"


def mayoractual(a, b, c):
    return max(a, b, c)

valor1 = 10  
result1 = mayoractual( 10, 20, 30)
print(f"El mayor entre 10, 20 y 30 es: {result1}")

result2 = mayoractual(100, 200, 50)
print(f"El mayor entre 100, 200 y 50 es: {result2}")

result3 = mayoractual(100, 50, 90)
print(f"El mayor entre 100, 50 y 90 es: {result3}")

result4 = mayoractual(40, 50, 50)
print(f"El mayor entre 40, 50 y 50 es: {result4}")

result5 = mayoractual(80, 80, 20)
print(f"El mayor entre 80, 80 y 20 es: {result5}")


