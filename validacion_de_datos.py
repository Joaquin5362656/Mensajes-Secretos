import doctest
import csv
from tkinter import END, messagebox



def validar_identificador(identificador):
    """
    Valida un identificador de usuario.

    >>> validar_identificador("usuario_123")
    True
    >>> validar_identificador("mi-usuario")
    True
    >>> validar_identificador("user.name")
    True
    >>> validar_identificador("abc123")
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
    >>> validar_identificador("test-123")
    True
    >>> validar_identificador("test.user")
    True
    >>> validar_identificador("long_username_123")
    False
    """
    longitud = len(identificador)
    es_largo = 5 <= longitud <= 15

    caracteres_permitidos = "_-."

    for caracter in identificador:
        if not (caracter.isalnum() or caracter in caracteres_permitidos):
            return False

    return es_largo

def validar_clave(clave):
    """
    Valida una clave de usuario.
    """
    longitud = len(clave)
    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_numero = False
    tiene_caracter_especial = False

    caracteres_especiales = "_-*#"

    if not 4 <= longitud <= 8:
        return False

    # Verificar caracteres repetidos adyacentes
    for i in range(longitud - 1):
        if clave[i] == clave[i + 1]:
            return False

    for caracter in clave:
        if caracter.isupper():
            tiene_mayuscula = True
        elif caracter.islower():
            tiene_minuscula = True
        elif caracter.isnumeric():
            tiene_numero = True
        elif caracter in caracteres_especiales:
            tiene_caracter_especial = True

    return tiene_mayuscula and tiene_minuscula and tiene_numero and tiene_caracter_especial

def solicitar_identificador():
    while True:

        identificador = input("Ingrese su identificador de usuario: ")

        if validar_identificador(identificador):
            print("Identificador válido. ¡Bienvenido!")
            return

        print("Identificador no válido. Asegúrese de cumplir con los requisitos.")

def solicitar_clave():
    while True:

        clave = input("Ingrese su clave de usuario: ")

        if validar_clave(clave):
            print("Clave válida. ¡Bienvenido!")
            return

        print("Clave no válida. Asegúrese de cumplir con los requisitos.")


def validar_registro_usuario(id_usuario, clave_usuario, id_pregunta, respuesta_recuperacion):
    intentos_recuperacion = 0  # Puedes ajustar esto según tus necesidades

    # Validar identificador
    if not validar_identificador(id_usuario):
        print("Identificador no válido. Asegúrese de cumplir con los requisitos.")
        messagebox.showinfo("Error", "Identificador no válido. Asegúrese de cumplir con los requisitos.")
        return

    # Validar contraseña
    if not validar_clave(clave_usuario):
        print("Contraseña no válida. Asegúrese de cumplir con los requisitos.")
        messagebox.showinfo("Error", "Contraseña no válida. Asegúrese de cumplir con los requisitos.")
        return

    try:
        # Cargar el archivo CSV existente
        with open('usuarios.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row and row[0] == id_usuario:
                    print("Identificador en uso")
                    messagebox.showinfo("Error", "Identificador en uso")
                    return
    except FileNotFoundError:
        print("No se encontró el archivo de usuarios. Creando uno nuevo...")

    # Continuar con el registro del usuario
    try:
        # Escribir en el archivo CSV
        with open('usuarios.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([id_usuario, clave_usuario, id_pregunta, respuesta_recuperacion, intentos_recuperacion])

        messagebox.showinfo("Éxito", "Usuario creado con éxito")
    except Exception as e:
        print(f"Error durante el registro: {e}")
        messagebox.showinfo("Error", "Ocurrió un error durante el registro. Por favor, inténtelo de nuevo.")


def main():
    solicitar_identificador()
    solicitar_clave()
    print(doctest.testmod())

if __name__ == "__main__":
    main()
