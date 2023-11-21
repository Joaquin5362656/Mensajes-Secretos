
def consultar_mensajes_recibidos(usuario):
    mensajes_usuario_particular = []
    mensajes_para_todos = []

    mensajes_totales = 0
    with open("mensajes.csv", "r") as mensajes:
        for linea in mensajes:
            destinatario, remitente, cifrado, mensaje_cifrado = linea.rstrip("\n").split(",")
    return