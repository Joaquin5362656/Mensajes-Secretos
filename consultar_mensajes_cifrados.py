import cifrado_atbash # archivos
import cifrado_cesar
CIFRADO_CESAR = "C"

def consultar_mensajes_recibidos(usuario):
    """
    Jennifer Mota: Funcion que recibe el usuario, verifica si el mensaje es para todos o para un usuario particular y si es cifrado Atbash o Cesar. De esa manera devuelve los mensajes recibidos decifrados y la cantidad de mensajes recibidos.
    """
    mensajes_usuario_particular = []
    mensajes_para_todos = []

    mensajes_totales = 0

    with open("mensajes.csv", "r") as mensajes:
        for linea in mensajes:
            destinatario, remitente, cifrado, mensaje_cifrado = linea.rstrip("\n").split(",")

            if usuario == destinatario:
                if cifrado == CIFRADO_CESAR:
                    mensaje_decifrado = cifrado_cesar.cifrar_string(mensaje_cifrado, -int(cifrado[1]))
                    mensaje = remitente + ":" + mensaje_decifrado
                    mensajes_usuario_particular.append(mensaje)
                else:
                    mensaje_decifrado = cifrado_atbash.cifrado_atbash(mensaje_cifrado)
                    mensaje = remitente + ":" + mensaje_decifrado
                    mensajes_usuario_particular.append(mensaje)
                mensajes_totales += 1

            elif destinatario == "*" and remitente != usuario:
                if cifrado == CIFRADO_CESAR:
                    mensaje_descifrado = cifrado_cesar.cifrar_string(mensaje_cifrado, -int(cifrado[1]))
                    mensaje = "#" + remitente +": " + mensaje_descifrado
                    mensajes_para_todos.append(mensaje)     
                else:
                    mensaje_descifrado = cifrado_atbash.cifrado_atbash(mensaje_cifrado)
                    mensaje = "#" + remitente +": " + mensaje_descifrado
                    mensajes_para_todos.append(mensaje)
                mensajes_totales += 1

        mensajes_recibidos = mensajes_para_todos + mensajes_usuario_particular

        return mensajes_recibidos, mensajes_totales