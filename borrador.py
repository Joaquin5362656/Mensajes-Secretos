NUMEROS = '1234567890'

B = 9


def cifrar_num(caracter, clave):
    posicion = NUMEROS.find(caracter)
    new_position = posicion + clave
    resta = 0
    if new_position <= B:
        new_caracter = NUMEROS[new_position]
    else:
        new_caracter = NUMEROS[new_position - B - 1]

    return new_caracter



def descifrar_string(string,clave):
    string_result = ''
    for caracter in string:
        new_caracter = cifrar_num(caracter, clave)
        string_result += new_caracter
    
    return string_result


string = '1'
clave = 20


print(descifrar_string(string, clave))