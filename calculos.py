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
