
ABECEDARIO_MIN = 'abcdefghijklmnñopqrstuvwxyz'
ABECEDARIO_MAY = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
NUMEROS = '1234567890'


def cifrar_may(caracter, clave):
    posicion = ABECEDARIO_MAY.find(caracter)
    new_position = (posicion + clave) % len(ABECEDARIO_MAY)
    return ABECEDARIO_MAY[new_position]


def cifrar_min(caracter, clave):
    posicion = ABECEDARIO_MIN.find(caracter)
    new_position = (posicion + clave) % len(ABECEDARIO_MIN)
    return ABECEDARIO_MIN[new_position]


def cifrar_num(caracter, clave):
    posicion = NUMEROS.find(caracter)
    new_position = (posicion + clave) % len(NUMEROS)
    return NUMEROS[new_position]
    


def detectar_caracter(caracter, clave):
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

import doctest
print(doctest.testmod())