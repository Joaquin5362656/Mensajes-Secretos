import doctest

# -*- coding: utf-8 -*-
ORIGINAL_MINUSCULA = 'abcdefghijklmnñopqrstuvwxyz'
ORIGINAL_MAYUSCULA = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
CLAVE_MAYUSCULA = 'ZYXWVUTSRQPOÑNMLKJIHGFEDCBA'
CLAVE_MINUSCULA = 'zyxwvutsrqpoñnmlkjihgfedcba'

def cifrado_atbash(texto):
    """
    Jennifer Mota: Se genera el cifrado y descifrado de Atbash. Que consiste en la 
    sustitucion de que cada letra del abecedario y se reemplaza por su inversa.

    Martin Ferreyra: Funcionamiento del caracter 'ñ' añadido

    >>> cifrado_atbash("HOLA MUNDO")
    'sloz ñfnwl'

    >>> cifrado_atbash("hola mundo")
    'SLOZ ÑFNWL'

    >>> cifrado_atbash("hOlA 1 munDO -")
    'SlOz 1 ÑFNwl -'

    >>> cifrado_atbash("SLOZ ÑFNWL")
    'hola mundo'

    >>> cifrado_atbash("SlOz 1 ÑFNwl -")
    'hOlA 1 munDO -'

    >>> cifrado_atbash("sloz ñfnwl")
    'HOLA MUNDO'
    """
    texto_cifrado = ""

    for letra in texto:
        if letra in ORIGINAL_MINUSCULA:
            indice = ORIGINAL_MINUSCULA.index(letra)
            texto_cifrado += CLAVE_MAYUSCULA [indice]

        elif letra in ORIGINAL_MAYUSCULA:
            indice = ORIGINAL_MAYUSCULA.index(letra)
            texto_cifrado += CLAVE_MINUSCULA [indice]

        else:
            texto_cifrado += letra
    return texto_cifrado


def main():
    # texto = input ("Introduce un texto: ")
    print(doctest.testmod())


if __name__ == "__main__":
    main()