from tkinter import *
from tkinter import messagebox
from cifrado_cesar import cifrar_string
from cifrado_atbash import cifrado_atbash


# Función para la ventana de bienvenida

def mostrar_ventana_bienvenida():
    '''Abre la primer ventana para interactuar con el usuario. Contiene boton para continuar a la segunda ventana.'''
    ventana_bienvenida = Tk()
    ventana_bienvenida.title("TP Grupal Parte 1- Grupo [Codeo]")
    ventana_bienvenida.iconbitmap("icono.ico")
    ventana_bienvenida.resizable(0,0)
    ventana_bienvenida.geometry("350x300")
    ventana_bienvenida.config(bg="#87CEFA")
    ventana_bienvenida.rowconfigure(0, weight=75)
    ventana_bienvenida.rowconfigure(3, weight=100)
    ventana_bienvenida.rowconfigure(6, weight=100)
    ventana_bienvenida.columnconfigure(0, weight=1)
    ventana_bienvenida.columnconfigure(3, weight=1)

    Label(ventana_bienvenida, text="Bienvenido a la aplicación\nde mensajes secretos del grupo [Codeo]").grid(row=1, column=1, columnspan=2, pady=10, sticky=W+E, ipady=5, ipadx=10)
    Button(ventana_bienvenida, text="Continuar", command=mostrar_ventana_principal).grid(row=2, column=1, columnspan=2, sticky=W+E)
    Label(ventana_bienvenida, text="Construída por", fg="#8c8c8c").grid(row=4, column=1, columnspan=2, pady=10, sticky=W+E+S, ipady=5)
    Label(ventana_bienvenida, text= "Joaquin Osorio\tJennifer Mota\nMartín Ferreyra\tDiego López", justify="left", fg="#8c8c8c").grid(row=5, column=1, columnspan=2, sticky=W+E, ipady=5)

    ventana_bienvenida.mainloop()



def mostrar_ventana_principal():
    """
    Función para la ventana principal y dentro de ella la funcion procesar_mensaje que, según la opción que se elija se hara
    el cifrado o descifrado correspondiente
    """

    def procesar_mensaje(opcion):
        mensaje = entry_mensaje.get()

        if opcion == "Cifrar Atbash":
            resultado = cifrado_atbash(mensaje)
        elif opcion == "Descifrar Atbash":
            resultado = cifrado_atbash(mensaje)  # Al ser Atbash, cifrar y descifrar es lo mismo
        elif opcion == "Cifrar César":
            clave = int(entry_clave.get())
            resultado = cifrar_string(mensaje, clave)
        elif opcion == "Descifrar César":
            clave = -int(entry_clave.get())  # Descifrar es cifrar con la clave negativa
            resultado = cifrar_string(mensaje, clave)
        else:
            resultado = "Opción no válida"

        messagebox.showinfo("Resultado", f"Resultado: {resultado}")


    # Configuraciones iniciales de la ventana

    ventana_principal = Tk()
    ventana_principal.title("TP Grupal Parte 1 - Grupo: [Codeo]")
    ventana_principal.iconbitmap("logo.ico")
    ventana_principal.resizable(0,0)
    ventana_principal.geometry("350x250")
    ventana_principal.config(bg="#00FA9A")
    ventana_principal.columnconfigure(0, weight=1)
    ventana_principal.columnconfigure(4, weight=1)
    ventana_principal.rowconfigure(0, weight=1)
    ventana_principal.rowconfigure(7, weight=1)


    # Labels y entrys

    Label(ventana_principal, text="Ingrese el mensaje:").grid(row=1, column=1, sticky=W+E, pady=5, ipadx=10, ipady=3)
    entry_mensaje = Entry(ventana_principal)
    entry_mensaje.grid(row=1, column=2, sticky=E, padx=5)

    Label(ventana_principal, text="Ingrese la clave (si aplica):").grid(row=2, column=1, sticky=W+E, pady=5, ipadx=10, ipady=3)
    entry_clave = Entry(ventana_principal)
    entry_clave.grid(row=2, column=2, sticky=E, padx=5)


    # Botones a partir de un for loop

    fila_boton = 3
    opciones = ["Cifrar Atbash", "Descifrar Atbash", "Cifrar César", "Descifrar César"]
    for opcion in opciones:
        Button(ventana_principal, text=opcion, command=lambda opc=opcion: procesar_mensaje(opc)).grid(row=fila_boton, column=1, columnspan=2, sticky=W+E, pady=5)
        fila_boton += 1

    ventana_principal.mainloop()


# Llama a la función de la ventana de bienvenida para iniciar la aplicación
mostrar_ventana_bienvenida()
