import cifrado_atbash # archivos
import cifrado_cesar
from tkinter import *
CIFRADO_CESAR = "C"


def leer_registro_mensaje(linea):
    """
    Martin Ferreyra: Funcion que procesa de forma correcta el caso en el que un mensaje
    incluya una coma, devolviendo todas las columnas del archivo csv posteriores a la del
    cifrado como un solo mensaje.
    """
    
    informacion = linea.rstrip().split(",")
    mensaje_cifrado = ", ".join(informacion[3:])

    destinatario = informacion[0]
    remitente = informacion[1]
    cifrado = informacion[2]

    return destinatario, remitente, cifrado, mensaje_cifrado


def consultar_mensajes_recibidos(usuario):
    """
    Jennifer Mota: Funcion que recibe el usuario, verifica si el mensaje es para todos
    o para un usuario particular y si es cifrado Atbash o Cesar. De esa manera devuelve
    los mensajes recibidos decifrados y la cantidad de mensajes recibidos.
    o para un usuario particular y si es cifrado Atbash o Cesar. De esa manera se obtiene
    los mensajes recibidos decifrados y la cantidad de mensajes recibidos para poder mostrarlos en la interfaz.
    """

    mensajes_usuario_particular = []
    mensajes_para_todos = []

    mensajes_totales = 0

    with open("./archivos csv/mensajes.csv", "r") as mensajes:
        for linea in mensajes:
            destinatario, remitente, cifrado, mensaje_cifrado = leer_registro_mensaje(linea)

            if (usuario == destinatario) or (destinatario == "*" and remitente != usuario):
                if cifrado[0] == CIFRADO_CESAR:
                    mensaje_decifrado = cifrado_cesar.cifrar_string(mensaje_cifrado, -int(cifrado[1]))

                else:
                    mensaje_decifrado = cifrado_atbash.cifrado_atbash(mensaje_cifrado)
                    mensaje = remitente + ": " + mensaje_decifrado
                    
                prefijo = "" if usuario == destinatario else "#"
                mensaje = prefijo + remitente + ": " + mensaje_decifrado
                mensajes_usuario_particular.append(mensaje)
                mensajes_totales += 1

        mensajes_recibidos = mensajes_para_todos + mensajes_usuario_particular

    mostrar_mensajes(mensajes_recibidos, mensajes_totales)


def mostrar_mensajes(mensajes_recibidos, mensajes_totales):
    """
    Martin Ferreyra: Funcion que genera una ventana con una barra de navegacion para visualizar
    todos los mensajes recibidos por el usuario registrado
    """
    
    ventana_de_mensajes = Toplevel()
    ventana_de_mensajes.title("Mensajes recibidos")
    ventana_de_mensajes.iconbitmap("./logos/logo.ico")
    ventana_de_mensajes.resizable(0, 0)
    ventana_de_mensajes.geometry("350x350")
    ventana_de_mensajes.config(bg="#87CEFA")

    barra_navegacion = Scrollbar(ventana_de_mensajes)
    cuadro_de_texto = Text(ventana_de_mensajes, height=200, width=200)

    barra_navegacion.pack(side=RIGHT, fill=Y)
    cuadro_de_texto.pack(side=LEFT, fill=Y)

    barra_navegacion.config(command=cuadro_de_texto.yview)
    cuadro_de_texto.config(yscrollcommand=barra_navegacion.set)

    texto = "Lista de mensajes:"
    for mensaje in mensajes_recibidos:
        texto = texto + "\n" + "-----------------------------------------" + "\n" + mensaje

    texto = texto + "\n"+ "-----------------------------------------" + "\n" + f"Mensajes totales: {mensajes_totales}"

    cuadro_de_texto.insert(END, texto)

    cuadro_de_texto.configure(state=DISABLED)
