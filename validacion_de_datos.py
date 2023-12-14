import doctest
import csv
from tkinter import END, messagebox



def validar_identificador(identificador):
    """
    Diego López: Valida un identificador de usuario.
    
    Requisitos:

    - Entre 5 y 15 caracteres
    - Formado solo por letras y numeros
    - Puede incluir los caracteres '_' '-' '.'

    >>> validar_identificador("usuario_123")
    True
    >>> validar_identificador("mi-usuario")
    True
    >>> validar_identificador("user.name")
    True
    >>> validar_identificador("user 123")
    False
    >>> validar_identificador("user_")
    True
    >>> validar_identificador("user@123")
    False
    >>> validar_identificador("user12345678901234")
    False
    >>> validar_identificador("aBc_DeF")
    True
    >>> validar_identificador("test.user")
    True
    >>> validar_identificador("long_username_123")
    False
    """

    es_valido = True
    
    # Checkear cantidad de caracteres
    es_largo = 5 <= len(identificador) <= 15

    caracteres_permitidos = "_-."

    # Iterar por cada caracter en lugar de iterar toda la cadena
    i = 0
    if es_largo:
        while es_valido and i < len(identificador):
            caracter = identificador[i]
            if not (caracter.isalnum() or caracter in caracteres_permitidos):
                es_valido = False
            i += 1
    else:
        es_valido = False

    return es_valido



def validar_clave(clave):
    """
    Diego López: Valida una clave de usuario.
    
    Requisitos:

    - Entre 4 y 8 caracteres
    - Al menos una mayuscula
    - Al menos una minuscula
    - Al menos un numero
    - Al menos uno de los caracteres '_' '-' '#' '*'
    - No caracteres repetidos adyacentes

    >>> validar_clave("Codeo_1")
    True
    >>> validar_clave("Coodeo_1")
    False
    >>> validar_clave("Codeo_")
    False
    >>> validar_clave("codeo_1")
    False
    >>> validar_clave("Codeo_12345")
    False
    >>> validar_clave("Codeo1")
    False
    >>> validar_clave("coodeo")
    False
    >>> validar_clave("codeo1")
    False
    >>> validar_clave("coodeoooooo")
    False
    >>> validar_clave("Codeo#0")
    True
    """

    # Variables de requisitos
    longitud_valida = 4 <= len(clave) <= 8
    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_numero = False
    tiene_caracter_especial = False
    no_caracteres_adyacentes = True

    caracteres_especiales = "_-*#"

    # Verificar caracteres repetidos adyacentes y cumplir longitud válida
    i = 0
    while i < len(clave) and longitud_valida:
        caracter = clave[i]

        if caracter.isupper():
            tiene_mayuscula = True
        elif caracter.islower():
            tiene_minuscula = True
        elif caracter.isnumeric():
            tiene_numero = True
        elif caracter in caracteres_especiales:
            tiene_caracter_especial = True

        # Verificar caracteres repetidos adyacentes
        if i < len(clave) - 1 and caracter == clave[i + 1]:
            no_caracteres_adyacentes = False

        i += 1

    return tiene_mayuscula and tiene_minuscula and tiene_numero and tiene_caracter_especial and no_caracteres_adyacentes



def validar_registro_usuario(id_usuario, clave_usuario, id_pregunta, respuesta_recuperacion):
    """
    Diego López: Funcion que se asegura de recibir toda la informacion completa
    para un registro de nuevo usuario.
    """
    
    # Busca usuario existente con mismo id
    if not buscar_usuario(id_usuario):
        
        # Verifica que los distintos campos sean validos
        if not validar_identificador(id_usuario):
            messagebox.showerror("Error", "Identificador no válido. Asegúrese de cumplir con los requisitos.")

        # Validar contraseña
        elif not validar_clave(clave_usuario):
            messagebox.showerror("Error", "Contraseña no válida. Asegúrese de cumplir con los requisitos.")

        # Validar campo de pregunta y respuesta
        elif id_pregunta == "Seleccione pregunta" or respuesta_recuperacion == "":
            messagebox.showerror("Error", "Pregunta o respuesta de recuperacion vacías.")
        
        else:
            guardar_nuevo_registro(id_usuario, clave_usuario, id_pregunta, respuesta_recuperacion)
        
    else:
        messagebox.showinfo("Error", "Identificador en uso")


def buscar_usuario(id_usuario):
    """
    Martin Ferreyra: Devuelve un usuario si lo encuentra o False
    en caso contrario.
    """
    with open('./archivos csv/usuarios.csv', 'r') as file:
        reader = csv.reader(file)
        row = next(reader, False)
        while row and row[0] != id_usuario:
            row = next(reader, False)
    return row


def checkear_bloqueo(id_usuario):
    """
    Martin Ferreyra: Funcion que lee el archivo de intentos de recuperacion
    y devuelve True o False en funcion de si el usuario esta bloqueado o no.
    """

    bloqueo = False
        
    with open("./archivos csv/recuperacion.csv", "r") as file:
        reader = csv.reader(file)

        for row in reader:
            if row and row[0] == id_usuario:
                if int(row[1]) > 2:
                    bloqueo = True

    return bloqueo


def guardar_nuevo_registro(id_usuario, clave_usuario, id_pregunta, respuesta_recuperacion):
    """
    Guarda un nuevo registro en el archivo de usuarios.
    """
    with open('./archivos csv/usuarios.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([id_usuario, clave_usuario, id_pregunta, respuesta_recuperacion, 0])

    messagebox.showinfo("Éxito", "Usuario creado con éxito")


# Funcion con propositos de testeo
def solicitar_identificador():
    identificador_no_valido = True
    
    while identificador_no_valido:

        identificador = input("Ingrese su identificador de usuario: ")

        if validar_identificador(identificador):
            identificador_no_valido = False
            print("Identificador válido. ¡Bienvenido!")
        else:
            print("Identificador no válido. Asegúrese de cumplir con los requisitos.")


# Funcion con propositos de testeo
def solicitar_clave():
    clave_no_valida = True

    while clave_no_valida:

        clave = input("Ingrese su clave de usuario: ")

        if validar_clave(clave):
            clave_no_valida = False
            print("Clave válida. ¡Bienvenido!")
        else:
            print("Clave no válida. Asegúrese de cumplir con los requisitos.")


def main():
    solicitar_identificador()
    solicitar_clave()
    print(doctest.testmod())

if __name__ == "__main__":
    main()
