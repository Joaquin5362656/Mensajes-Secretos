from tkinter import *
from tkinter import ttk, messagebox
from cifrado_cesar import cifrar_string
from cifrado_atbash import cifrado_atbash
from validacion_de_datos import validar_registro_usuario
import csv


# Función para la ventana de bienvenida
def mostrar_ventana_bienvenida():
    '''Abre la primer ventana para interactuar con el usuario. Contiene boton para continuar a la segunda ventana.
        Diego López y Martin Ferreyra
    '''
    ventana_bienvenida = Tk()
    ventana_bienvenida.title("TP Grupal Parte 1- Grupo [Codeo]")
    ventana_bienvenida.iconbitmap("./logos/icono.ico")
    ventana_bienvenida.resizable(0, 0)
    ventana_bienvenida.geometry("350x300")
    ventana_bienvenida.config(bg="#87CEFA")
    ventana_bienvenida.rowconfigure(0, weight=50)
    ventana_bienvenida.rowconfigure(3, weight=100)
    ventana_bienvenida.rowconfigure(6, weight=100)
    ventana_bienvenida.columnconfigure(0, weight=1)
    ventana_bienvenida.columnconfigure(3, weight=1)

    Label(ventana_bienvenida, text="Bienvenido a la aplicación\nde mensajes secretos del grupo [Codeo]\n Para continuar presione continuar, \nde lo contrario cierre la ventana").grid(row=1, column=1, columnspan=2, pady=15, sticky=W+E, ipady=5, ipadx=10)
    Button(ventana_bienvenida, text="Crear Usuario", command=mostrar_ventana_registro).grid(row=2, column=1, columnspan=2, sticky=W+E)
    Button(ventana_bienvenida, text="Ingreso Usuario", command=mostrar_ventana_ingreso).grid(row=3, column=1, columnspan=2, sticky=W+E)
    Label(ventana_bienvenida, text="Construída por", fg="#8c8c8c").grid(row=4, column=1, columnspan=2, pady=10, sticky=W+E+S, ipady=5)
    Label(ventana_bienvenida, text="Joaquin Osorio\tJennifer Mota\nMartín Ferreyra\tDiego López", justify="left", fg="#8c8c8c").grid(row=5, column=1, columnspan=2, sticky=W+E, ipady=5)

    ventana_bienvenida.mainloop()


def mostrar_ventana_registro():

    # Configuracion ventana
    ventana_registro = Toplevel()
    ventana_registro.title("Registro de usuario")
    ventana_registro.iconbitmap("./logos/icono.ico")
    ventana_registro.resizable(0, 0)
    ventana_registro.geometry("350x300")
    ventana_registro.config(bg="#87CEFA")
    ventana_registro.rowconfigure(0, weight=1)
    ventana_registro.rowconfigure(4, weight=1)
    ventana_registro.rowconfigure(8, weight=1)
    ventana_registro.columnconfigure(0, weight=1)
    ventana_registro.columnconfigure(3, weight=1)  


    # Labels y botones
    Label(ventana_registro, text="Ingrese un usuario:").grid(row=1, column=1, sticky=W+E, pady=5, padx=5)
    Label(ventana_registro, text="Ingrese una clave").grid(row=2, column=1, sticky=W+E, pady=5, padx=5)

    entry_usuario = Entry(ventana_registro)
    entry_usuario.grid(row=1, column=2)

    entry_clave = Entry(ventana_registro)
    entry_clave.grid(row=2, column=2)

    # Menu desplegable
    with open("./archivos csv/preguntas.csv") as file:
        preguntas = []
        reader = csv.reader(file)
        for row in reader:
            preguntas.append(row[1])

    desplegable_preguntas = ttk.Combobox(ventana_registro, values=preguntas)
    desplegable_preguntas.set("Seleccione pregunta")
    desplegable_preguntas.grid(row=3, column=1, sticky=W+E, pady=5, padx=5)

    entry_respuesta_pregunta = Entry(ventana_registro)
    entry_respuesta_pregunta.grid(row=3, column=2, sticky=W+E, pady=10, padx=5)

    # Boton para registrar
    Button(ventana_registro, text="Registrar",command= lambda: validar_registro_usuario(entry_usuario.get(), entry_clave.get(), desplegable_preguntas.get(), entry_respuesta_pregunta.get())).grid(row=5, column=1, columnspan=2, sticky=W+E, pady=10)

    # Requisitos
    Label(ventana_registro, text="El identificador debe estar compuesto solo de\nletras, numeros o los caracteres '_' '-' y '.'\ny debe tener minimo 5 y maximo 15 caracteres", justify="left", fg="#8c8c8c").grid(row=6, column=1, columnspan=2, sticky=W+E, pady=5)
    Label(ventana_registro, text="Requisitos de la clave:\n- De 4 a 8 caracteres\t- Al menos un numero\n- Al menos una mayuscula\t- Incluye '_' '-' '#' o '*'\n- Al menos una minuscula\t- Adyacentes no repetidos", justify="left", fg="#8c8c8c").grid(row=7, column=1, columnspan=2)


def mostrar_ventana_ingreso():

    # Configuracion ventana
    ventana_ingreso = Toplevel()
    ventana_ingreso.title("Identificación para acceso")
    ventana_ingreso.iconbitmap("./logos/icono.ico")
    ventana_ingreso.resizable(0, 0)
    ventana_ingreso.geometry("350x200")
    ventana_ingreso.config(bg="#87CEFA")
    ventana_ingreso.rowconfigure(0, weight=1)
    ventana_ingreso.rowconfigure(3, weight=1)
    ventana_ingreso.rowconfigure(6, weight=1)
    ventana_ingreso.columnconfigure(0, weight=1)
    ventana_ingreso.columnconfigure(3, weight=1)


    # Labels y entrys
    Label(ventana_ingreso, text="Ingrese su usuario:").grid(row=1, column=1, sticky=W+E, pady=5, ipadx=10, ipady=1)
    entry_usuario_ingreso = Entry(ventana_ingreso)
    entry_usuario_ingreso.grid(row=1, column=2, sticky=E, padx=5)

    Label(ventana_ingreso, text="Ingrese su clave:").grid(row=2, column=1, sticky=W+E, pady=5, ipadx=10, ipady=1)
    entry_clave_ingreso = Entry(ventana_ingreso, show="*")
    entry_clave_ingreso.grid(row=2, column=2, sticky=E, padx=5)

    Button(ventana_ingreso, text="Ingresar", command=lambda: validar_ingreso(ventana_ingreso, entry_usuario_ingreso.get(), entry_clave_ingreso.get())).grid(row=4, column=1, columnspan=2, sticky=W+E)
    Button(ventana_ingreso, text="He olvidado mi contraseña", command= ventana_recuperar_clave).grid(row=5, column=1, columnspan=2, sticky=W+E, pady=5)
    
    # Vincula la tecla Enter al botón
    entry_clave_ingreso.bind("<Return>", lambda event=None: validar_ingreso(ventana_ingreso, entry_usuario_ingreso.get(), entry_clave_ingreso.get()))


def ventana_recuperar_clave():

    # Configuracion ventana
    ventana_recuperacion = Toplevel()
    ventana_recuperacion.title("Recuperación clave")
    ventana_recuperacion.iconbitmap("./logos/icono.ico")
    ventana_recuperacion.resizable(0, 0)
    ventana_recuperacion.geometry("350x250")
    ventana_recuperacion.config(bg="#87CEFA")
    ventana_recuperacion.rowconfigure(0, weight=1)
    ventana_recuperacion.rowconfigure(4, weight=1)
    ventana_recuperacion.rowconfigure(6, weight=1)
    ventana_recuperacion.columnconfigure(0, weight=1)
    ventana_recuperacion.columnconfigure(1, weight=1)
    ventana_recuperacion.columnconfigure(2, weight=1)
    ventana_recuperacion.columnconfigure(3, weight=1)

    # Labels y entrys
    Label(ventana_recuperacion, text="Si ha olvidado su contraseña,\npor favor complete todos los campos.").grid(row=1, column=1, columnspan=2, sticky=W+E, pady=5, ipady=5)
    Label(ventana_recuperacion, text="Ingrese su usuario:").grid(row=2, column=1, sticky=W+E, pady=5, ipady=1)
    
    entry_usuario_recuperacion = Entry(ventana_recuperacion)
    entry_usuario_recuperacion.grid(row=2, column=2, sticky=W+E, padx=5)

    
    # Desplegable de preguntas
    with open("./archivos csv/preguntas.csv") as file:
        preguntas = []
        reader = csv.reader(file)
        for row in reader:
            preguntas.append(row[1])

    desplegable_preguntas = ttk.Combobox(ventana_recuperacion, values=preguntas)
    desplegable_preguntas.set("Seleccione pregunta")
    desplegable_preguntas.grid(row=3, column=1, sticky=W+E, pady=5, padx=5)

    entry_respuesta_pregunta = Entry(ventana_recuperacion)
    entry_respuesta_pregunta.grid(row=3, column=2, sticky=W+E, pady=10, padx=5)

    Button(ventana_recuperacion, text="Recuperar", command= lambda: recuperar_clave(entry_usuario_recuperacion.get(), desplegable_preguntas.get(), entry_respuesta_pregunta.get())).grid(row=5, column=1, columnspan=2, sticky=W+E)


def recuperar_clave(id_usuario, id_pregunta, respuesta_recuperacion):
    entradas_validas = False

    with open('./archivos csv/usuarios.csv', 'r+') as file:
        reader = csv.reader(file)
        writer = csv.writer(file)
        for row in reader:
            if row and row[0] == id_usuario and row[2] == id_pregunta and row[3] == respuesta_recuperacion:
                messagebox.showinfo("Éxito", f"Su contraseña es: {row[1]}")
                entradas_validas = True
            elif row and row[0] == id_usuario and (row[2] != id_pregunta or row[3] != respuesta_recuperacion):
                messagebox.showerror("Error", "Respuesta incorrecta")
                row[4] = int(row[4]) + 1
                entradas_validas = True
                writer.writerow([row[0],row[1],row[2],row[3],row[4]])
    
    if not entradas_validas:
        messagebox.showerror("Error", "Verifique los datos")



def validar_ingreso(ventana_ingreso, id_usuario_ingreso, clave_ingreso):
    ingreso_exitoso = False

    with open('./archivos csv/usuarios.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] == id_usuario_ingreso and row[1] == clave_ingreso and int(row[4]) <= 3:
                ingreso_exitoso = True
                messagebox.showinfo("Éxito", "Ingreso exitoso")
                ventana_ingreso.destroy()  # Cerrar la ventana de ingreso
                mostrar_ventana_principal()  # Abrir la ventana principal
            elif row and row[0] == id_usuario_ingreso and int(row[4]) > 3:
                ingreso_exitoso = True
                messagebox.showerror("Error", "Usuario bloqueado")

    if not ingreso_exitoso:
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
        else:
            resultado = "Opción no válida"

        messagebox.showinfo("Resultado", f"Resultado: {resultado}")

    # Configuraciones iniciales de la ventana
    ventana_principal = Tk()
    ventana_principal.title("TP Grupal Parte 1 - Grupo: [Codeo]")
    ventana_principal.iconbitmap("./logos/logo.ico")
    ventana_principal.resizable(0, 0)
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
