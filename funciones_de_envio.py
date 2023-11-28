from tkinter import *
from tkinter import messagebox
from cifrado_cesar import cifrar_string
from cifrado_atbash import cifrado_atbash
import csv
ARCHIVO_USUARIOS = "./archivos csv/usuarios.csv"
ARCHIVO_MENSAJES = "./archivos csv/mensajes.csv"


def leer_archivo(archivo):
    """
    Esta función lee una línea del archivo CSV y devuelve un registro como lista.
    """
    linea = archivo.readline()
    if linea:
        registro = linea.rstrip().split(",")
    else:
        registro = []
    return registro


def checkear_bloqueo(id_usuario):
        bloqueo = False
        
        with open("./archivos csv/recuperacion.csv", "r") as file:
            reader = csv.reader(file)

            for row in reader:
                if row and row[0] == id_usuario:
                    if int(row[1]) > 3:
                        bloqueo = True

        return bloqueo


def verificar_destinatario(destinatario, id_usuario):
    """Funcion que verifica si el usuario al que se le desea enviar el msj existe en el archivo usuarios.csv"""
    encontrado = False

    with open(ARCHIVO_USUARIOS,'r') as file:
        registro = leer_archivo(file)

        while registro and not encontrado:
            if registro[0] == destinatario or destinatario == "*":
                encontrado = True
            registro = leer_archivo(file)


    bloqueado = checkear_bloqueo(destinatario)

    if bloqueado:
        encontrado = False
        messagebox.showerror("Error", "El destinatario está bloqueado")

    if destinatario == id_usuario:
        encontrado = False
        messagebox.showerror("Error", "El destinatario es usted mismo")

    if not encontrado:
        messagebox.showerror("Error", "Destinatario Inexistente")

    return encontrado


def ventana_cesar(id_usuario):
    """Funcion que muestra una ventana para proseguir con el envio del mensaje con el cifrado cesar"""
    # Configuraciones iniciales de la ventana
    ventana_cesar = Toplevel()
    ventana_cesar.title("Cifrado Cesar - Grupo: [Codeo]")
    ventana_cesar.iconbitmap("./logos/logo.ico")
    ventana_cesar.resizable(0, 0)
    ventana_cesar.geometry("400x150")
    ventana_cesar.config(bg="#00FA9A")
    ventana_cesar.columnconfigure(0, weight=1)
    ventana_cesar.columnconfigure(4, weight=1)
    ventana_cesar.rowconfigure(0, weight=1)
    ventana_cesar.rowconfigure(7, weight=1)

    # Labels
    Label(ventana_cesar, text="Ingrese el destinatario:").grid(row=1, column=1, sticky=W+E, pady=5, ipadx=10, ipady=1)
    entry_destinatario = Entry(ventana_cesar)
    entry_destinatario.grid(row=1, column=2, sticky=E, padx=5)

    # Botón para verificar el destinatario
    boton_verificar = Button(ventana_cesar, text="Verificar", command=lambda: habilitar_opciones_cesar(entry_destinatario.get()))
    boton_verificar.grid(row=1, column=3, padx=5, sticky=W+E)


    def habilitar_opciones_cesar(destinatario):
        """#Funcion que verifica a quien se les va a enviar el mensaje"""
        encontrado = verificar_destinatario(destinatario, id_usuario)

        if encontrado:
            entry_destinatario.config(state=DISABLED)
            boton_verificar.config(state=DISABLED)

            # Mostrar el Label y el Entry para escribir una oración
            Label(ventana_cesar, text="Ingrese una oración:").grid(row=2, column=1, sticky=W+E, pady=5, ipadx=10, ipady=1)
            entry_oracion = Entry(ventana_cesar)
            entry_oracion.grid(row=2, column=2, columnspan=2, sticky=W+E, padx=5)
            Label(ventana_cesar, text="Ingrese una Clave:").grid(row=3, column=1, sticky=W+E, pady=5, ipadx=10, ipady=1)
            entry_clave = Entry(ventana_cesar)
            entry_clave.grid(row=3, column=2, sticky=E, padx=5)

            boton_enviar = Button(ventana_cesar, text="Enviar", command=lambda: enviar_mensaje_cesar(entry_destinatario.get(), entry_oracion.get(), entry_clave.get(), boton_enviar, cifrar_string))
            boton_enviar.grid(row=3, column=3, padx=5, sticky=W+E)


    def enviar_mensaje_cesar(destinatario, oracion, clave, boton_enviar):
        """Funcion que guarda los datos en un archivo.csv"""
        
        if oracion and clave:
            mensaje = cifrar_string(oracion, clave)
            cifrado_mas_clave = 'C' + clave

            with open(ARCHIVO_MENSAJES, "a") as archivo_mensaje:
                archivo_mensaje.write(f'{destinatario},{id_usuario},{cifrado_mas_clave},{mensaje}\n')
            
            entry_destinatario.config(state=NORMAL)
            boton_verificar.config(state=NORMAL)
            boton_enviar.config(state=DISABLED)

            messagebox.showinfo("Éxito", "Envio exitoso")


def ventana_atbash(id_usuario):
    """Funcion que muestra una ventana para proseguir con el envio del mensaje con el cifrado atbash"""
    cifrado = 'cifrado_atbash'
    # Configuraciones iniciales de la ventana
    ventana_atbash = Toplevel()
    ventana_atbash.title("Cifrado Atbash - Grupo: [Codeo]")
    ventana_atbash.iconbitmap("./logos/logo.ico")
    ventana_atbash.resizable(0, 0)
    ventana_atbash.geometry("400x150")
    ventana_atbash.config(bg="#00FA9A")
    ventana_atbash.columnconfigure(0, weight=1)
    ventana_atbash.columnconfigure(4, weight=1)
    ventana_atbash.rowconfigure(0, weight=1)
    ventana_atbash.rowconfigure(7, weight=1)

    #labels
    Label(ventana_atbash, text="Ingrese el destinatario:").grid(row=1, column=1, sticky=W+E, pady=5, ipadx=10, ipady=3)
    entry_destinatario = Entry(ventana_atbash)
    entry_destinatario.grid(row=1, column=2, sticky=E, padx=5)

    # Botón para verificar el destinatario
    boton_verificar = Button(ventana_atbash, text="Verificar", command= lambda: habilitar_opciones_atbash(entry_destinatario.get()))
    boton_verificar.grid(row=1, column=3, padx=5)


    def habilitar_opciones_atbash(destinatario):
        """Funcion que verifica a quien se les va a enviar el mensaje"""
        encontrado = verificar_destinatario(destinatario, id_usuario)

        if encontrado:
            entry_destinatario.config(state=DISABLED)
            boton_verificar.config(state=DISABLED)

            # Mostrar el Label y el Entry para escribir una oración
            Label(ventana_atbash, text="Ingrese una oración:").grid(row=2, column=1, sticky=W+E, pady=5, ipadx=10, ipady=3)
            entry_oracion = Entry(ventana_atbash)
            entry_oracion.grid(row=2, column=2, sticky=E, padx=5)
            boton_enviar = Button(ventana_atbash, text="Enviar", command=lambda: enviar_mensaje_atbash(entry_destinatario.get(), entry_oracion.get(), boton_enviar))
            boton_enviar.grid(row=2, column=3, padx=5, sticky=W+E)

    
    def enviar_mensaje_atbash(destinatario, oracion, boton_enviar):
        """Funcion que guarda los datos en un archivo.csv"""
        
        if oracion:
            mensaje = cifrado_atbash(oracion)

            with open(ARCHIVO_MENSAJES, "a") as archivo_mensaje:
                archivo_mensaje.write(f'{destinatario},{id_usuario},A,{mensaje}\n')
            
            entry_destinatario.config(state=NORMAL)
            boton_verificar.config(state=NORMAL)
            boton_enviar.config(state=DISABLED)

            messagebox.showinfo("Éxito", "Envio exitoso")

