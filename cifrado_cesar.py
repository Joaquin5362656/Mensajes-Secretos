
ABECEDARIO_MIN = 'abcdefghijklmnñopqrstuvwxyz'
ABECEDARIO_MAY = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
NUMEROS = '1234567890'
A = 26
B = 9

def cifrar_may(caracter, clave):
    posicion = ABECEDARIO_MAY.find(caracter)
    new_position = posicion + clave
    if new_position <= A:
        new_caracter = ABECEDARIO_MAY[new_position]
    else:
        new_caracter = ABECEDARIO_MAY[new_position - A - 1]

    return new_caracter


def cifrar_min(caracter, clave):
    posicion = ABECEDARIO_MIN.find(caracter)
    new_position = posicion + clave
    if new_position <= A:
        new_caracter = ABECEDARIO_MIN[new_position]
    else:
        new_caracter = ABECEDARIO_MIN[new_position - A - 1]

    return new_caracter

def cifrar_num(caracter, clave):
    posicion = NUMEROS.find(caracter)
    new_position = posicion + clave
    if new_position <= B:
        new_caracter = NUMEROS[new_position]
    else:
        new_caracter = NUMEROS[new_position - B - 1]

    return new_caracter
    


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

"""caracter = '0'
clave = 10
print(detectar_caracter(caracter, clave))"""


def descifrar_string(string,clave):

    """
    >>> descifrar_string("521", 3)
    '854'

    >>> descifrar_string("521ad", 1)
    '632be'

    >>> descifrar_string("aeiu", 0)
    'aeiu'

    >>> descifrar_string("AI120", 10)
    'KR120'

    >>> descifrar_string("1  2 32AH", 2)
    '3  4 54CJ'

    >>> descifrar_string("###", -1)
    '###'

    >>> descifrar_string("52", -1)
    '41'

    >>> descifrar_string("AbZ", -1)
    'ZaY'

    >>> descifrar_string("XWER 121 $%&//%/ Aadsf", 18)
    'OÑVJ 909 $%&//%/ Rrukw'

    >>> descifrar_string("ASD __adsaUU1", -4)
    'WOZ __wzowQQ7'
    """
    
    string_result = ''
    for caracter in string:
        new_caracter = detectar_caracter(caracter, clave)
        string_result += new_caracter
    
    return string_result

import doctest
print(doctest.testmod())