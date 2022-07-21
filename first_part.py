"""
1. Crear una función que pase de entero > 0 y > 4000 a romano
2. Cualquier otra entrada debe dar error


"""

class RomanNumberError(Exception):
    pass

numero_romano = {
    1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'
}

algoritmo_romano = (
    {1: 'M'},
    {1: 'C', 5: 'D', 10: 'M'},
    {1: 'X', 5: 'L', 10: 'C'},
    {1: 'I', 5: 'V', 10: 'X'},
)

componentes = {
    
    1000: 'M', 2000: 'MM', 3000: 'MMM',
    100: 'C', 200: 'CC', 300: 'CCC',
    400: 'CD', 500: 'D', 600: 'DC',
    700: 'DCC', 800: 'DCCC', 900: 'CM',
    10: 'X', 20: 'XX', 30: 'XXX',
    40: 'XL', 50: 'L', 60: 'LX',
    70: 'LXX', 80: 'LXXX', 90: 'XC',
    1: 'I', 2: 'II', 3: 'III',
    4: 'IV', 5: 'V', 6: 'VI',
    7: 'VII', 8: 'VIII', 9: 'IX',
}

def entero_a_romano_2(numero):
    numero = "{:0>4d}".format(numero)
    digitos = list(numero)

    romano = ""

    for digito in digitos:
        digito = int(digito)  
    
        if digito < 4:
            romano += algoritmo_romano[0][1] * digito
        elif int(digitos[1]) == 4:
            romano += numero_romano[100] + numero_romano[500]
        elif int(digitos[1]) < 9:
            romano += numero_romano[500] + numero_romano[100] * (int(digitos[1]) - 5)
        else:
            romano += numero_romano[100] + numero_romano[1000]

    if int(digitos[2]) < 4:
        romano += numero_romano[10] * int(digitos[0])
    elif int(digitos[2]) == 4:
        romano += numero_romano[10] + numero_romano[50]
    elif int(digitos[2]) < 9:
        romano += numero_romano[50] + numero_romano[10] * (int(digitos[2]) - 5)
    else:
        romano += numero_romano[10] + numero_romano[100]
    
    if int(digitos[3]) < 4:
        romano += numero_romano[1] * int(digitos[0])
    elif int(digitos[3]) == 4:
        romano += numero_romano[1] + numero_romano[5]
    elif int(digitos[3]) < 9:
        romano += numero_romano[5] + numero_romano[1] * (int(digitos[3]) - 5)
    else:
        romano += numero_romano[1] + numero_romano[10]




def entero_a_romano(numero):
    '''
    numero = str(numero)
    longitud = len(numero)

    if longitud < 4:
        numero = "{:0>4s}".format(numero)
    '''
    numero = "{:0>4d}".format(numero)
    digitos = list(numero)

    ix = 0
    longitud = len(digitos)
    romano = ""
    for ix in range(len(numero)):
        longitud -= 1
        digitos[ix] = digitos[ix] + "0" * longitud
        romano += componentes.get(int(digitos[ix]), "")
          
    return romano
    

entero_a_romano(336)
