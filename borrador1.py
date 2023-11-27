from tkinter import *
from tkinter import ttk, messagebox
from cifrado_cesar import cifrar_string
from cifrado_atbash import cifrado_atbash
from validacion_de_datos import validar_registro_usuario
from borrador2 import ventana_cesar
from borrador2 import ventana_atbash
import csv

"""
Este borrador seria la version antigua de interfaz_grafica.py, con la que trabaje de base para el objetivo 2
Solo agregue 2 botones en la funcion procesar_mensajes() y un return row[0] en la funcion validar_ingreso como
intento de querer importar la funcion a borrador2.py y obtener el usuario (me tira error)
"""




# Función para agregar preguntas
def agregar_preguntas():
    nuevas_preguntas = [
        (6, "Color favorito"),
        (7, "Comida preferida"),
        (8, "Lugar de nacimiento"),
        (9, "Libro favorito"),
        (10, "Hobby principal"),
    ]

    # Leer preguntas existentes del archivo
    preguntas_existentes = []
    with open('preguntas.csv', 'r', newline='', encoding='utf-8') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        preguntas_existentes = list(lector_csv)

    # Agregar nuevas preguntas
    for nueva_pregunta in nuevas_preguntas:
        preguntas_existentes.append(nueva_pregunta)

    # Guardar preguntas actualizadas en el archivo
    with open('preguntas.csv', 'w', newline='', encoding='utf-8') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerows(preguntas_existentes)

agregar_preguntas()
# Función para la ventana de bienvenida
def mostrar_ventana_bienvenida():
    '''Abre la primer ventana para interactuar con el usuario. Contiene boton para continuar a la segunda ventana.
        Diego López y Martin Ferreyra
    '''
    ventana_bienvenida = Tk()
    ventana_bienvenida.title("TP Grupal Parte 1- Grupo [Codeo]")
    ventana_bienvenida.iconbitmap("icono.ico")
    ventana_bienvenida.resizable(0, 0)
    ventana_bienvenida.geometry("350x300")
    ventana_bienvenida.config(bg="#87CEFA")
    ventana_bienvenida.rowconfigure(0, weight=75)
    ventana_bienvenida.rowconfigure(3, weight=100)
    ventana_bienvenida.rowconfigure(6, weight=100)
    ventana_bienvenida.columnconfigure(0, weight=1)
    ventana_bienvenida.columnconfigure(3, weight=1)

    Label(ventana_bienvenida, text="Bienvenido a la aplicación\nde mensajes secretos del grupo [Codeo]\n Para continuar presione continuar, \nde lo contrario cierre la ventana").grid(row=1, column=1, columnspan=2, pady=10, sticky=W+E, ipady=5, ipadx=10)
    Button(ventana_bienvenida, text="Crear Usuario", command=mostrar_ventana_registro).grid(row=2, column=1, columnspan=2, sticky=W+E)
    Button(ventana_bienvenida, text="Ingreso Usuario", command=mostrar_ventana_ingreso).grid(row=3, column=1, columnspan=2, sticky=W+E)
    Label(ventana_bienvenida, text="Construída por", fg="#8c8c8c").grid(row=4, column=1, columnspan=2, pady=10, sticky=W+E+S, ipady=5)
    Label(ventana_bienvenida, text="Joaquin Osorio\tJennifer Mota\nMartín Ferreyra\tDiego López", justify="left", fg="#8c8c8c").grid(row=5, column=1, columnspan=2, sticky=W+E, ipady=5)

    ventana_bienvenida.mainloop()


# Variables globales para almacenar datos de registro
usuario_var = None
clave_var = None
pregunta_var = None
respuesta_var = None
ventana_registro = None


# Función para la ventana de registro
def mostrar_ventana_registro():
    def validar_campos():
        global usuario_var, clave_var, pregunta_var, respuesta_var

        usuario_var = entry_usuario.get()
        clave_var = entry_clave.get()
        pregunta_var = combo_preguntas.get()
        respuesta_var = entry_respuesta.get()

        if not usuario_var or not clave_var or pregunta_var == "Seleccione una pregunta" or not respuesta_var:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")
            return False

        return True

    def validar_registro():
        if validar_campos():
            
            validar_registro_usuario(usuario_var, clave_var, pregunta_var, respuesta_var)

    global ventana_registro
    ventana_registro = Tk()
    ventana_registro.title("TP Grupal Parte 1- Grupo [Codeo]")
    ventana_registro.iconbitmap("icono.ico")
    ventana_registro.resizable(0, 0)
    ventana_registro.geometry("350x300")
    ventana_registro.config(bg="#87CEFA")
    ventana_registro.rowconfigure(0, weight=75)
    ventana_registro.rowconfigure(3, weight=100)
    ventana_registro.rowconfigure(6, weight=100)
    ventana_registro.columnconfigure(0, weight=1)
    ventana_registro.columnconfigure(3, weight=1)

    Label(ventana_registro, text="Ingrese un usuario:").grid(row=1, column=1, sticky=W+E, pady=5, ipadx=10, ipady=3)
    entry_usuario = Entry(ventana_registro)
    entry_usuario.grid(row=1, column=2, sticky=E, padx=5)

    Label(ventana_registro, text="Ingrese una clave:").grid(row=2, column=1, sticky=W+E, pady=5, ipadx=10, ipady=3)
    entry_clave = Entry(ventana_registro, show="*")
    entry_clave.grid(row=2, column=2, sticky=E, padx=5)

    preguntas = [
        "Apellido de su abuela materna",
        "Nombre de tu mascota",
        "Nombre de tu mejor amigo/amiga",
        "Cantante preferido",
        "Ciudad preferida"
    ]
    combo_preguntas = ttk.Combobox(ventana_registro, values=preguntas)
    combo_preguntas.set("Seleccione una pregunta")
    combo_preguntas.grid(row=3, column=1, sticky=E, padx=15, pady=5)

    Label(ventana_registro, text="Ingrese su respuesta:").grid(row=4, column=1, sticky=W+E, pady=5, ipadx=10, ipady=3)
    entry_respuesta = Entry(ventana_registro, show="*")
    entry_respuesta.grid(row=4, column=2, sticky=E, padx=5)

    Button(ventana_registro, text="Crear Usuario", command=validar_registro).grid(row=5, column=1, columnspan=2, sticky=W+E)

def mostrar_ventana_ingreso():
    ventana_ingreso = Toplevel()
    ventana_ingreso.title("Identificación para acceso")
    ventana_ingreso.geometry("350x300")
    ventana_ingreso.config(bg="#87CEFA")
    ventana_ingreso.rowconfigure(0, weight=75)
    ventana_ingreso.rowconfigure(3, weight=100)
    ventana_ingreso.rowconfigure(6, weight=100)
    ventana_ingreso.columnconfigure(0, weight=1)
    ventana_ingreso.columnconfigure(3, weight=1)

    Label(ventana_ingreso, text="Ingrese su usuario:").grid(row=0, column=0, sticky=W+E, pady=5, ipadx=10, ipady=3)
    entry_usuario_ingreso = Entry(ventana_ingreso)
    entry_usuario_ingreso.grid(row=0, column=1, sticky=E, padx=5)

    Label(ventana_ingreso, text="Ingrese su clave:").grid(row=1, column=0, sticky=W+E, pady=5, ipadx=10, ipady=3)
    entry_clave_ingreso = Entry(ventana_ingreso, show="*")
    entry_clave_ingreso.grid(row=1, column=1, sticky=E, padx=5)

    Button(ventana_ingreso, text="Ingresar", command=lambda: validar_ingreso(ventana_ingreso, entry_usuario_ingreso, entry_clave_ingreso)).grid(row=2, column=1, columnspan=2, sticky=W+E)
    Button(ventana_ingreso, text="He olvidado mi contraseña", command= recuperacion_clave).grid(row=3, column=1, columnspan=2, sticky=W+E)
    # Vincula la tecla Enter al botón
    entry_clave_ingreso.bind("<Return>", lambda event=None: validar_ingreso(ventana_ingreso, entry_usuario_ingreso, entry_clave_ingreso))

def recuperacion_clave():
    ventana_recuperacion= Toplevel()
    ventana_recuperacion.title("recuperación clave")
    ventana_recuperacion.geometry("350x300")
    ventana_recuperacion.config(bg="#87CEFA")
    ventana_recuperacion.rowconfigure(0, weight=75)
    ventana_recuperacion.rowconfigure(3, weight=100)
    ventana_recuperacion.rowconfigure(6, weight=100)
    ventana_recuperacion.columnconfigure(0, weight=1)
    ventana_recuperacion.columnconfigure(3, weight=1)

    Label(ventana_recuperacion, text="Si ha olvidado su contraseña,por favor complete todos los campos.").grid(row=0, column=0, sticky=W+E, pady=5, ipadx=10, ipady=3)
    Label(ventana_recuperacion, text="Ingrese su usuario:").grid(row=1, column=0, sticky=W+E, pady=5, ipadx=10, ipady=3)
    entry_usuario_recuperacion = Entry(ventana_recuperacion)
    entry_usuario_recuperacion.grid(row=1, column=1, sticky=E, padx=5)

    
def validar_ingreso(ventana_ingreso, entry_usuario_ingreso, entry_clave_ingreso):
    id_usuario_ingreso = entry_usuario_ingreso.get()
    clave_ingreso = entry_clave_ingreso.get()

    with open('usuarios.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] == id_usuario_ingreso and row[1] == clave_ingreso:
                messagebox.showinfo("Éxito", "Ingreso exitoso")
                ventana_ingreso.destroy()  # Cerrar la ventana de ingreso
                mostrar_ventana_principal()  # Abrir la ventana principal
                return row[0]                                                      #Agregado para el objetivo 2 

    messagebox.showerror("Error", "Ingreso fallido. Verifica tus credenciales.")
    


def mostrar_ventana_principal():
    """
    Función para la ventana principal y dentro de ella la función procesar_mensaje que, según la opción que se elija se hará
    el cifrado o descifrado correspondiente.
    Diego López y Martín Ferreyra
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
        elif opcion == "Enviar Mensaje Cifrado César":              #Agregado para el objetivo 2
            abrir = ventana_cesar()                                 #Agregado para el objetivo 2
        elif opcion == "Enviar Mensaje Cifrado Atbash":             #Agregado para el objetivo 2
            abrir = ventana_atbash()                                #Agregado para el objetivo 2
        else:
            resultado = "Opción no válida"

        if opcion not in ["Enviar Mensaje Cifrado César", "Enviar Mensaje Cifrado Atbash"]:
            messagebox.showinfo("Resultado", f"Resultado: {resultado}")

    # Configuraciones iniciales de la ventana
    ventana_principal = Toplevel()
    ventana_principal.title("TP Grupal Parte 1 - Grupo: [Codeo]")
    ventana_principal.iconbitmap("logo.ico")
    ventana_principal.resizable(0, 0)
    ventana_principal.geometry("350x300")
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
    opciones = ["Cifrar Atbash", "Descifrar Atbash", "Cifrar César", "Descifrar César", "Enviar Mensaje Cifrado César", "Enviar Mensaje Cifrado Atbash"]
    for opcion in opciones:
        Button(ventana_principal, text=opcion, command=lambda opc=opcion: procesar_mensaje(opc)).grid(row=fila_boton, column=1, columnspan=2, sticky=W+E, pady=5)
        fila_boton += 1

    ventana_principal.mainloop()

# Llama a la función de la ventana de bienvenida para iniciar la aplicación
mostrar_ventana_bienvenida()


print(validar_ingreso)