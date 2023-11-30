import cifrado_atbash # archivos
import cifrado_cesar
from tkinter import *
CIFRADO_CESAR = "C"

def consultar_mensajes_recibidos(usuario):
    """
    Jennifer Mota: Funcion que recibe el usuario, verifica si el mensaje es para todos
    o para un usuario particular y si es cifrado Atbash o Cesar. De esa manera se obtiene
    los mensajes recibidos decifrados y la cantidad de mensajes recibidos para poder mostrarlos en la interfaz.
    """
    mensajes_usuario_particular = []
    mensajes_para_todos = []

    mensajes_totales = 0

    with open("./archivos csv/mensajes.csv", "r") as mensajes:
        for linea in mensajes:
            destinatario, remitente, cifrado, mensaje_cifrado = linea.rstrip("\n").split(",")

            if usuario == destinatario:
                if cifrado[0] == CIFRADO_CESAR:
                    mensaje_decifrado = cifrado_cesar.cifrar_string(mensaje_cifrado, -int(cifrado[1]))
                    mensaje = remitente + ": " + mensaje_decifrado
                    mensajes_usuario_particular.append(mensaje)
                else:
                    mensaje_decifrado = cifrado_atbash.cifrado_atbash(mensaje_cifrado)
                    mensaje = remitente + ": " + mensaje_decifrado
                    mensajes_usuario_particular.append(mensaje)
                mensajes_totales += 1

            elif destinatario == "*" and remitente != usuario:
                if cifrado[0] == CIFRADO_CESAR:
                    mensaje_descifrado = cifrado_cesar.cifrar_string(mensaje_cifrado, -int(cifrado[1]))
                    mensaje = "#" + remitente +": " + mensaje_descifrado
                    mensajes_para_todos.append(mensaje)     
                else:
                    mensaje_descifrado = cifrado_atbash.cifrado_atbash(mensaje_cifrado)
                    mensaje = "#" + remitente +": " + mensaje_descifrado
                    mensajes_para_todos.append(mensaje)
                mensajes_totales += 1

        mensajes_recibidos = mensajes_para_todos + mensajes_usuario_particular

    mostrar_mensajes(mensajes_recibidos, mensajes_totales)


def mostrar_mensajes(mensajes_recibidos, mensajes_totales):
    """
    Funcion que genera una ventana con una barra de navegacion para visualizar
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
