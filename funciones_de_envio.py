from tkinter import *
from tkinter import messagebox
from cifrado_cesar import cifrar_string
from cifrado_atbash import cifrado_atbash
from validacion_de_datos import checkear_bloqueo, buscar_usuario
import csv
ARCHIVO_USUARIOS = "./archivos csv/usuarios.csv"
ARCHIVO_MENSAJES = "./archivos csv/mensajes.csv"
"""
Martin Ferreyra: Reformulacion completa del archivo
"""

def ventana_cesar(id_usuario):
    """
    Joaquin Osorio: Funcion que muestra una ventana para proseguir con el envio 
    del mensaje con el cifrado cesar.
    """

    # Configuraciones iniciales de la ventana
    ventana_cesar = Toplevel()
    ventana_cesar.title("Cifrado Cesar - Grupo: [Codeo]")
    ventana_cesar.iconbitmap("./logos/logo.ico")
    ventana_cesar.resizable(0, 0)
    ventana_cesar.geometry("400x200")
    ventana_cesar.config(bg="#00FA9A")
    ventana_cesar.columnconfigure(0, weight=1)
    ventana_cesar.columnconfigure(4, weight=1)
    ventana_cesar.rowconfigure(0, weight=1)
    ventana_cesar.rowconfigure(7, weight=1)

    # Labels
    Label(ventana_cesar, text="Ingrese el destinatario:").grid(row=1, column=1, sticky=W+E, pady=5, ipadx=10, ipady=1)
    Label(ventana_cesar, text="Ingrese una oración:").grid(row=2, column=1, sticky=W+E, pady=5, ipadx=10, ipady=1)
    Label(ventana_cesar, text="Ingrese una Clave:").grid(row=3, column=1, sticky=W+E, pady=5, ipadx=10, ipady=1)

    entry_destinatario = Entry(ventana_cesar)
    entry_destinatario.grid(row=1, column=2, sticky=E, padx=5)

    entry_oracion = Entry(ventana_cesar)
    entry_oracion.grid(row=2, column=2, columnspan=2, sticky=W+E, padx=5)
    
    entry_clave = Entry(ventana_cesar)
    entry_clave.grid(row=3, column=2, sticky=E, padx=5)

    # Botón para verificar el destinatario
    boton_verificar = Button(ventana_cesar, text="Enviar", command=lambda: verificar_destinatario(entry_destinatario.get(), id_usuario, entry_oracion.get(), 0, entry_clave.get()))
    boton_verificar.grid(row=4, column=1, columnspan=2, pady=5, sticky=W+E)


def ventana_atbash(id_usuario):
    """
    Joaquin Osorio: Funcion que muestra una ventana para proseguir con el envio del mensaje
    con el cifrado atbash.
    """

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
    ventana_atbash.rowconfigure(4, weight=1)

    #labels
    Label(ventana_atbash, text="Ingrese el destinatario:").grid(row=1, column=1, sticky=W+E, pady=5, ipadx=10, ipady=3)
    Label(ventana_atbash, text="Ingrese una oración:").grid(row=2, column=1, sticky=W+E, pady=5, ipadx=10, ipady=3)

    entry_destinatario = Entry(ventana_atbash)
    entry_destinatario.grid(row=1, column=2, sticky=E, padx=5)

    entry_oracion = Entry(ventana_atbash)
    entry_oracion.grid(row=2, column=2, sticky=E, padx=5)

    # Botón para verificar el destinatario
    boton_verificar = Button(ventana_atbash, text="Verificar", command= lambda: verificar_destinatario(entry_destinatario.get(), id_usuario, entry_oracion.get(), 1))
    boton_verificar.grid(row=3, column=1, columnspan=2, sticky=W+E, pady=5)


def verificar_destinatario(id_destinatario, id_usuario, oracion, cifrador, clave=False):
    """
    Joaquin Osorio: Funcion que verifica si el usuario al que se le desea enviar el msj existe 
    en el archivo usuarios.csv.
    """

    """
    Martin Ferreyra: Esta comprobacion esta hecha intencionalmente de esta manera aprovechando el
    short-circuit, si el destinatario es '*' no se buscará innecesariamente en el archivo csv
    """
    if (id_destinatario == "*" or buscar_usuario(id_destinatario)):
        if id_destinatario == id_usuario:
            messagebox.showerror("Error", "El destinatario es usted mismo")

        elif checkear_bloqueo(id_destinatario):
            messagebox.showerror("Error", "Destinatario bloqueado")
        
        else:
            if not oracion:
                messagebox.showerror("Error", "Introduzca un mensaje")
            
            else:
                if cifrador == 0:
                    enviar_mensaje_cesar(id_destinatario, id_usuario, oracion, clave)
                elif cifrador == 1:
                    enviar_mensaje_atbash(id_destinatario, id_usuario, oracion)
    else:
        messagebox.showerror("Error", "Destinatario inexistente")


def enviar_mensaje_cesar(destinatario, id_usuario, oracion, clave):
    """
    Joaquin Osorio: Funcion que guarda los datos en un archivo.csv.
    """
        
    if clave.isnumeric():
        mensaje = cifrar_string(oracion, clave)
        cifrado_mas_clave = 'C' + clave

        with open(ARCHIVO_MENSAJES, "a") as archivo_mensaje:
            archivo_mensaje.write(f'{destinatario},{id_usuario},{cifrado_mas_clave},{mensaje}\n')

        messagebox.showinfo("Éxito", "Envio exitoso")
    
    else:
        messagebox.showerror("Error", "Coloque una clave numerica")


def enviar_mensaje_atbash(destinatario, id_usuario, oracion):
    """
    Joaquin Osorio: Funcion que guarda los datos en un archivo.csv.
    """
    
    if oracion:
        mensaje = cifrado_atbash(oracion)

        with open(ARCHIVO_MENSAJES, "a") as archivo_mensaje:
            archivo_mensaje.write(f'{destinatario},{id_usuario},A,{mensaje}\n')

            messagebox.showinfo("Éxito", "Envio exitoso")
