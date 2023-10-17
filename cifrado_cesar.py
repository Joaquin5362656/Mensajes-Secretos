
ABECEDARIO_MIN = 'abcdefghijklmnopqrstuvwxyz'
ABECEDARIO_MAY = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
NUMEROS = '1234567890'
A = 25
B = 9

def cifrar_may(caracter, clave):
    posicion = ABECEDARIO_MAY.find(caracter)
    new_position = posicion + clave
    if new_position + clave <= A:
        new_caracter = ABECEDARIO_MAY[new_position]
    else:
        new_caracter = ABECEDARIO_MAY[new_position - A - 1]

    return new_caracter


def cifrar_min(caracter, clave):
    posicion = ABECEDARIO_MIN.find(caracter)
    new_position = posicion + clave
    if new_position + clave <= A:
        new_caracter = ABECEDARIO_MIN[new_position]
    else:
        new_caracter = ABECEDARIO_MIN[new_position - A - 1]

    return new_caracter

def cifrar_num(caracter, clave):
    posicion = NUMEROS.find(caracter)
    new_position = posicion + clave
    if new_position + clave <= B:
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
clave = 3
print(detectar_caracter(caracter, clave))"""


def descifrar_string(string,clave):
    
    string_result = ''
    for caracter in string:
        new_caracter = detectar_caracter(caracter, clave)
        string_result += new_caracter
    
    return string_result

string = 'Hola mundo"##$ 12'
clave = 3
print(descifrar_string(string,clave))