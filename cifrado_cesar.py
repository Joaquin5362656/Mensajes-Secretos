import doctest

# -*- coding: utf-8 -*-
ABECEDARIO_MIN = 'abcdefghijklmnñopqrstuvwxyz'
ABECEDARIO_MAY = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
NUMEROS = '1234567890'


def cifrar_may(caracter, clave):    
    """
    Joaquin Osorio: Funcion que recibe como parametros un caracter y una clave, ubica la posicion del caracter dentro de las
    constantes globales y con la clave se desplaza al nuevo indice correspondiente, esto retorna el caracter cifrado
    Funcion hecha por Joaquin Osorio
    """
    posicion = ABECEDARIO_MAY.find(caracter)
    new_position = (posicion + int(clave)) % len(ABECEDARIO_MAY)
    return ABECEDARIO_MAY[new_position]


def cifrar_min(caracter, clave):
    """
    Joaquin Osorio: Funcion que recibe como parametros un caracter y una clave, ubica la posicion del caracter dentro de las
    constantes globales y con la clave se desplaza al nuevo indice correspondiente, esto retorna el caracter cifrado
    Funcion hecha por Joaquin Osorio
    """
    posicion = ABECEDARIO_MIN.find(caracter)
    new_position = (posicion + int(clave)) % len(ABECEDARIO_MIN)
    return ABECEDARIO_MIN[new_position]


def cifrar_num(caracter, clave):
    """
    Joaquin Osorio: Funcion que recibe como parametros un caracter y una clave, ubica la posicion del caracter dentro de las
    constantes globales y con la clave se desplaza al nuevo indice correspondiente, esto retorna el caracter cifrado
    Funcion hecha por Joaquin Osorio
    """
    posicion = NUMEROS.find(caracter)
    new_position = (posicion + int(clave)) % len(NUMEROS)
    return NUMEROS[new_position]
    


def detectar_caracter(caracter, clave):
    """
    Joaquin Osorio: Funcion que reciber un caracter y una clave como parametros y comprueba si el caracter estan dentro
    de las constantes globables, dependiendo de que tipo de caracter sea, llama a su respectiva funcion
    que cifra el caracter y retorna el caracter cifrado
    Funcion hecha por Joaquin Osorio
    """
    if caracter in ABECEDARIO_MAY:
        new_caracter = cifrar_may(caracter, clave)
    elif caracter in ABECEDARIO_MIN:
        new_caracter = cifrar_min(caracter, clave)
    elif caracter in NUMEROS:
        new_caracter = cifrar_num(caracter, clave)
    else:
        new_caracter = caracter

    return new_caracter


def cifrar_string(string,clave):
    """
    Joaquin Osorio: Funcion que se encarga de ietrar sobre el string que se le pasa como parametro y llama a la funcion detectar caracter
    y recibe el caracter cifrado con su respectiva clave. Concatena todos los caracteres cifrados y retorna el string cifrado 
    Funcion hecha por Joaquin Osorio
    
    
    >>> cifrar_string("521", 3)
    '854'

    >>> cifrar_string("521ad", 1)
    '632be'

    >>> cifrar_string("632be", -1)
    '521ad'

    >>> cifrar_string("AI120", 10)
    'KR120'

    >>> cifrar_string("1  2 32AH", 2)
    '3  4 54CJ'

    >>> cifrar_string("###", -1)
    '###'

    >>> cifrar_string("52", -1)
    '41'

    >>> cifrar_string("AbZ", -1)
    'ZaY'

    >>> cifrar_string("XWER 121 $%&//%/ Aadsf", 20)
    'QPXL 121 $%&//%/ Ttwmy'

    >>> cifrar_string("ASD __adsaUU1", -4)
    'WOZ __wzowQQ7'
    """
    
    string_result = ''
    for caracter in string:
        new_caracter = detectar_caracter(caracter, clave)
        string_result += new_caracter
    
    return string_result


def main():
    print(doctest.testmod())


if __name__ == "__main__":
    main()