import tkinter as tk
from tkinter import messagebox
from cifrado_cesar import cifrar_string
from cifrado_atbash import cifrado_atbash


# Función para la ventana de bienvenida
def mostrar_ventana_bienvenida():
    ventana_bienvenida = tk.Tk()
    ventana_bienvenida.title("TP Grupal Parte 1- Grupo [Codeo]")
    # Escribo la ruta del archivo completa,ya que mi pc no me lo toma de otra manera. Para que funcione en codigo,deberian borrar la ruta y 
    # dejar entre comillas icono.ico.
    ventana_bienvenida.iconbitmap(r"C:\Users\vvilo\OneDrive\Escritorio\algo1\icono.ico")
    ventana_bienvenida.resizable(0,0)
    ventana_bienvenida.geometry("350x350")
    ventana_bienvenida.config(bg="#87CEFA")
    tk.Label(ventana_bienvenida, text="Bienvenido a la aplicación de mensajes secretos del grupo [Codeo]").pack()
    tk.Button(ventana_bienvenida, text="Continuar", command=mostrar_ventana_principal).pack()
    tk.Label(ventana_bienvenida, text="Construída por:").pack()

    integrantes = ["Joaquin Osorio", "Jennifer Mota", "Óscar Ferreyra", "Diego López"]
    for integrante in integrantes:
        tk.Label(ventana_bienvenida, text=integrante).pack()

    ventana_bienvenida.mainloop()

# Función para la ventana principal y dentro de ella la funcion procesar_mensaje que, según la opción que se elija se hara
# el cifrado o descifrado de la clave
def mostrar_ventana_principal():
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

    ventana_principal = tk.Tk()
    ventana_principal.title("TP Grupal Parte 1 - Grupo: [Codeo]")
    ventana_principal.iconbitmap(r"C:\Users\vvilo\OneDrive\Escritorio\algo1\logo.ico")#Misma resolucion que la anterior.
    ventana_principal.resizable(0,0)
    ventana_principal.geometry("350x350")
    ventana_principal.config(bg="#00FA9A")

    tk.Label(ventana_principal, text="Ingrese el mensaje:").pack()
    entry_mensaje = tk.Entry(ventana_principal)
    entry_mensaje.pack()

    tk.Label(ventana_principal, text="Ingrese la clave (si aplica):").pack()
    entry_clave = tk.Entry(ventana_principal)
    entry_clave.pack()

    opciones = ["Cifrar Atbash", "Descifrar Atbash", "Cifrar César", "Descifrar César"]
    for opcion in opciones:
        tk.Button(ventana_principal, text=opcion, command=lambda opc=opcion: procesar_mensaje(opc)).pack()

    ventana_principal.mainloop()

# Llama a la función de la ventana de bienvenida para iniciar la aplicación
mostrar_ventana_bienvenida()
