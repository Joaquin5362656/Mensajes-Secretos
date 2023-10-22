import doctest

ORIGINAL_MINUSCULA = 'abcdefghijklmnopqrstuvwxyz'
ORIGINAL_MAYUSCULA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
CLAVE_MAYUSCULA = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
CLAVE_MINUSCULA = 'zyxwvutsrqponmlkjihgfedcba'

def cifrado_atbash(texto):
    # Jennifer Mota: Se genera el cifrado y descifrado atbash
    """
    >>> cifrado_atbash("HOLA MUNDO")
    'sloz nfmwl'

    >>> cifrado_atbash("hola mundo")
    'SLOZ NFMWL'

    >>> cifrado_atbash("hOlA 1 munDO -")
    'SlOz 1 NFMwl -'

    >>> cifrado_atbash("SLOZ NFMWL")
    'hola mundo'

    >>> cifrado_atbash("SlOz 1 NFMwl -")
    'hOlA 1 munDO -'
    """
    texto_cifrado = ""

    for letra in texto:
        if letra in ORIGINAL_MINUSCULA:
            # Identifica la posición de cada letra
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
main()      