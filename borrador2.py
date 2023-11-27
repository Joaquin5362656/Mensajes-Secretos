from tkinter import *
from tkinter import messagebox
from cifrado_cesar import cifrar_string
from cifrado_atbash import cifrado_atbash
#from borrador1 import validar_ingreso
import csv
ARCHIVO_USUARIOS = "usuarios.csv"
MAX = "ZZZZ"
ARCHIVO_MENSAJES = 'mensajes.csv'
#REMITENTE = validar_ingreso()



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


def verificar_destinatario(destinatario, registro_actual=None):
    """Funcion que verifica si el usuario al que se le desea enviar el msj existe en el archivo usuarios.csv"""
    result = False
    encontrado = False

    with open(ARCHIVO_USUARIOS,'r') as file:
        registro = leer_archivo(file)

        while registro and registro != MAX and not encontrado:
            if registro[0] == destinatario and registro != registro_actual:
                result = True
                encontrado = True
            registro = leer_archivo(file)

    return result 

    
def ventana_cesar():
    """Funcion que muestra una ventana para proseguir con el envio del mensaje con el cifrado cesar"""
    # Configuraciones iniciales de la ventana
    ventana_cesar = Toplevel()
    ventana_cesar.title("Cifrado Cesar - Grupo: [Codeo]")
    ventana_cesar.iconbitmap("logo.ico")
    ventana_cesar.resizable(0, 0)
    ventana_cesar.geometry("355x210")
    ventana_cesar.config(bg="#00FA9A")
    ventana_cesar.columnconfigure(0, weight=1)
    ventana_cesar.columnconfigure(4, weight=1)
    ventana_cesar.rowconfigure(0, weight=1)
    ventana_cesar.rowconfigure(7, weight=1)

    #labels
    Label(ventana_cesar, text="Ingrese el destinatario:").grid(row=1, column=1, sticky=W+E, pady=5, ipadx=10, ipady=3)
    entry_mensaje = Entry(ventana_cesar)
    entry_mensaje.grid(row=1, column=2, sticky=E, padx=5)

    def verificar_y_mostrar():
        """#Funcion que verifica a quien se les va a enviar el mensaje """
        destinatario = entry_mensaje.get()
        encontrado = verificar_destinatario(destinatario)

        if encontrado or "*":
            # Mostrar el Label y el Entry para escribir una oración
            Label(ventana_cesar, text="Ingrese una oración:").grid(row=2, column=1, sticky=W+E, pady=5, ipadx=10, ipady=3)
            entry_oracion = Entry(ventana_cesar)
            entry_oracion.grid(row=2, column=2, sticky=E, padx=5)
            Label(ventana_cesar, text="Ingrese una Clave:").grid(row=3, column=1, sticky=W+E, pady=5, ipadx=10, ipady=3)
            entry_clave = Entry(ventana_cesar)
            entry_clave.grid(row=3, column=2, sticky=E, padx=5)

            
            def enviar_mensaje1():
                """Funcion que guarda los datos en un archivo.csv"""
                oracion = entry_oracion.get()
                mensaje = cifrar_string(oracion,int(entry_clave.get()))
                cifrado_mas_clave = 'C' + str(entry_clave.get())
                
                if destinatario != "*":
                    with open(ARCHIVO_MENSAJES, "a") as archivo_mensaje:
                        archivo_mensaje.write(f'{destinatario}, {cifrado_mas_clave}, {mensaje}\n')              #NECESITO EL USUARIO PARA AGREGARLO EN EL ARCHIVO MENSAJES.CSV
                    messagebox.showinfo("Éxito", "Envio exitoso")
                    ventana_cesar.destroy()
                else:
                    with open(ARCHIVO_MENSAJES, "a") as archivo_mensajes, open(ARCHIVO_USUARIOS, "r") as archivo_usuarios:
                        continuar = True
                        while continuar:
                            registro = leer_archivo(archivo_usuarios)
                            if registro:
                                usuario = registro[0]
                                archivo_mensajes.write(f'{usuario}, {cifrado_mas_clave}, {mensaje}\n')                #NECESITO EL USUARIO PARA AGREGARLO EN EL ARCHIVO MENSAJES.CSV
                            else:
                                continuar = False
                    ventana_cesar.destroy()
                    messagebox.showinfo("Éxito", "Envio exitoso")


            boton_enviar = Button(ventana_cesar, text="Enviar", command=enviar_mensaje1)
            boton_enviar.grid(row=3, column=3, padx=5)
        else:
            messagebox.showerror("Error", "El destinatario no se encuentra en el archivo CSV.")

    # Botón para verificar el destinatario
    boton_verificar = Button(ventana_cesar, text="Verificar", command=verificar_y_mostrar)
    boton_verificar.grid(row=1, column=3, padx=5)

def ventana_atbash():
    """Funcion que muestra una ventana para proseguir con el envio del mensaje con el cifrado atbash"""
    cifrado = 'cifrado_atbash'
    # Configuraciones iniciales de la ventana
    ventana_atbash = Toplevel()
    ventana_atbash.title("Cifrado Atbash - Grupo: [Codeo]")
    ventana_atbash.iconbitmap("logo.ico")
    ventana_atbash.resizable(0, 0)
    ventana_atbash.geometry("350x150")
    ventana_atbash.config(bg="#00FA9A")
    ventana_atbash.columnconfigure(0, weight=1)
    ventana_atbash.columnconfigure(4, weight=1)
    ventana_atbash.rowconfigure(0, weight=1)
    ventana_atbash.rowconfigure(7, weight=1)

    #labels
    Label(ventana_atbash, text="Ingrese el destinatario:").grid(row=1, column=1, sticky=W+E, pady=5, ipadx=10, ipady=3)
    entry_usuario = Entry(ventana_atbash)
    entry_usuario.grid(row=1, column=2, sticky=E, padx=5)

    def verificar_y_mostrar():
        """Funcion que verifica a quien se les va a enviar el mensaje  """
        destinatario = entry_usuario.get()
        encontrado = verificar_destinatario(destinatario)

        if encontrado or "*":
            # Mostrar el Label y el Entry para escribir una oración
            Label(ventana_atbash, text="Ingrese una oración:").grid(row=2, column=1, sticky=W+E, pady=5, ipadx=10, ipady=3)
            entry_oracion = Entry(ventana_atbash)
            entry_oracion.grid(row=2, column=2, sticky=E, padx=5)

            
            def enviar_mensaje2():
                """Funcion que guarda los datos en un archivo.csv"""
                oracion = entry_oracion.get()
                mensaje = cifrado_atbash(oracion)
                
                if destinatario != "*":
                    with open(ARCHIVO_MENSAJES, "a") as archivo_mensaje:
                        archivo_mensaje.write(f'{destinatario}, {cifrado}, {mensaje}\n')    #NECESITO EL USUARIO PARA AGREGARLO EN EL ARCHIVO MENSAJES.CSV
                    messagebox.showinfo("Éxito", "Envio exitoso")
                    ventana_atbash.destroy()
                else:
                    with open(ARCHIVO_MENSAJES, "a") as archivo_mensajes, open(ARCHIVO_USUARIOS, "r") as archivo_usuarios:
                        continuar = True
                        while continuar:
                            registro = leer_archivo(archivo_usuarios)
                            if registro:
                                usuario = registro[0]
                                archivo_mensajes.write(f'{usuario}, {cifrado}, {mensaje}\n')           #NECESITO EL USUARIO PARA AGREGARLO EN EL ARCHIVO MENSAJES.CSV
                            else:
                                continuar = False
                    ventana_atbash.destroy()
                    messagebox.showinfo("Éxito", "Envio exitoso")

            boton_enviar = Button(ventana_atbash, text="Enviar", command=enviar_mensaje2)
            boton_enviar.grid(row=2, column=3, padx=5)
        else:
            messagebox.showerror("Error", "El destinatario no se encuentra en el archivo CSV.")

    # Botón para verificar el destinatario
    boton_verificar = Button(ventana_atbash, text="Verificar", command=verificar_y_mostrar)
    boton_verificar.grid(row=1, column=3, padx=5)