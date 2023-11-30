from tkinter import *
from tkinter import ttk, messagebox
from cifrado_cesar import cifrar_string
from cifrado_atbash import cifrado_atbash
from validacion_de_datos import validar_registro_usuario, checkear_bloqueo
from funciones_de_envio import ventana_atbash
from funciones_de_envio import ventana_cesar
from consultar_mensajes_cifrados import consultar_mensajes_recibidos
import csv
import os


# Función para la ventana de bienvenida
def mostrar_ventana_bienvenida():
    """
    Diego López y Martin Ferreyra: Abre la primer ventana para interactuar con el usuario. 
    Contiene boton para continuar a la segunda ventana.
    """

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
    """
    Diego López: Ventana de registro para nuevos usuarios con su
    correspondiente validacion posterior.

    Martin Ferreyra: Modificaciones visuales.
    """

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
    """
    Diego López: Ventana de acceso en la que se colocan todos los
    datos del usuario ingresante para su posterior checkeo.

    Martin Ferreyra: Modificaciones visuales.
    """

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
    """
    Martin Ferreyra: Se abre una pestaña correspondiente a la recuperacion de clave,
    el usuario ingresado para la recuperacion tiene que existir y no estar bloqueado.
    """

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
    """
    Martin Ferreyra: Funcion ejecutada en el intento de recuperacion de clave
    en la ventana 'Recuperacion de clave' que maneja los distintos escenarios,
    es decir: Si se dio un usuario valido, si la pregunta o respuesta de
    recuperacion son incorrectas, si el usuario se encuentra bloqueado, etc. 
    """

    entradas_validas = False
    bloqueado = checkear_bloqueo(id_usuario)

    with open('./archivos csv/usuarios.csv', 'r') as file:
        reader = csv.reader(file)

        for row in reader:
            if row and row[0] == id_usuario and row[2] == id_pregunta and row[3] == respuesta_recuperacion:
                if bloqueado:
                    messagebox.showerror("Error", "Usuario bloqueado")
                    entradas_validas = True

                else:
                    messagebox.showinfo("Éxito", f"Su contraseña es: {row[1]}")
                    actualizar_intentos_recuperacion(row, reinicio=True)
                    entradas_validas = True

            elif row and row[0] == id_usuario and (row[2] != id_pregunta or row[3] != respuesta_recuperacion):
                if bloqueado:
                    messagebox.showerror("Error", "Usuario bloqueado")
                    entradas_validas = True

                else:
                    messagebox.showerror("Error", "Respuesta incorrecta")
                    actualizar_intentos_recuperacion(row)
                    entradas_validas = True
    
    if not entradas_validas:
        messagebox.showerror("Error", "Verifique los datos")


def actualizar_intentos_recuperacion(datos_usuario, reinicio=False):
    """
    Martin Ferreyra: En caso de introducitse un usuario valido en la ventana de
    'Recuperacion de clave', esta funcion evalua actualiza los intentos de
    recuperacion, sumando uno o reiniciando la cuenta de intentos.
    """

    registro_existente = False

    # Abrir los registros existentes de intentos de recuperacion
    with open("./archivos csv/recuperacion.csv", "r+") as datos_recuperaciones:
        reader = csv.reader(datos_recuperaciones)

        # Abrir nuevo archivo en donde se registra la informacion existente mas la actualizacion
        with open("./archivos csv/actualizacion.csv", "x+", newline='') as actualizacion:
            writer = csv.writer(actualizacion)

            # Recorrer lineas de registros existentes
            for row in reader:
                if row and row[0] == datos_usuario[0] and int(row[1]) <= 3:
                    if reinicio:
                        writer.writerow([datos_usuario[0],0])
                        registro_existente = True
                    else:
                        writer.writerow([datos_usuario[0],int(row[1]) + 1])
                        registro_existente = True
                elif row and row[0] == datos_usuario[0] and int(row[1]) > 3:
                    messagebox.showerror("Error", "Usuario Bloqueado")
                    writer.writerow([datos_usuario[0],int(row[1]) + 1])
                    registro_existente = True
                else:
                    writer.writerow(row)
            
            # Si el usuario no existia en el archivo, se agrega
            if not registro_existente:
                writer.writerow([datos_usuario[0],1])
            
    os.remove("./archivos csv/recuperacion.csv")
    os.rename("./archivos csv/actualizacion.csv", "./archivos csv/recuperacion.csv")


def validar_ingreso(ventana_ingreso, id_usuario_ingreso, clave_ingreso):
    """
    Diego López: Funcion que valida el ingreso del usuario si sus datos, es decir,
    su id_usuario y su clave, son las mismas que en el archivo usuarios.csv.

    Martin Ferreyra: Agregado el escenario en el que el usuario introducido sea
    un usuario bloqueado, cuyo caso se niega el acceso con una advertencia.
    """
    
    ingreso_exitoso = False

    # Determinamos si el usuario existe y si la clave es correcta
    with open('./archivos csv/usuarios.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] == id_usuario_ingreso and row[1] == clave_ingreso:
                ingreso_exitoso = True
                bloqueado = checkear_bloqueo(id_usuario_ingreso)

                if bloqueado:
                    messagebox.showerror("Error", "Usuario bloqueado")
                else:
                    messagebox.showinfo("Éxito", "Ingreso exitoso")
                    ventana_ingreso.destroy()  # Cerrar la ventana de ingreso
                    mostrar_ventana_principal(id_usuario_ingreso)  # Abrir la ventana principal

    if not ingreso_exitoso:
        messagebox.showerror("Error", "Ingreso fallido. Verifica tus credenciales.")


def mostrar_ventana_principal(id_usuario):
    """
    Diego López y Martín Ferreyra: Función para la ventana principal y dentro de 
    ella la función procesar_mensaje que, según la opción que se elija se hará
    el cifrado o descifrado correspondiente.
    """

    # Configuraciones iniciales de la ventana
    ventana_principal = Toplevel()
    ventana_principal.title("Cifrado y envío de mensajes")
    ventana_principal.iconbitmap("./logos/logo.ico")
    ventana_principal.resizable(0, 0)
    ventana_principal.geometry("350x400")
    ventana_principal.config(bg="#00FA9A")
    ventana_principal.columnconfigure(0, weight=1)
    ventana_principal.columnconfigure(4, weight=1)
    ventana_principal.rowconfigure(0, weight=1)
    ventana_principal.rowconfigure(10, weight=1)

    # Labels y entrys
    Label(ventana_principal, text="Ingrese el mensaje:").grid(row=1, column=1, sticky=W+E, pady=5, ipadx=10, ipady=1)
    entry_mensaje = Entry(ventana_principal)
    entry_mensaje.grid(row=1, column=2, sticky=E, padx=5)

    Label(ventana_principal, text="Ingrese la clave (si aplica):").grid(row=2, column=1, sticky=W+E, pady=5, ipadx=10, ipady=1)
    entry_clave = Entry(ventana_principal)
    entry_clave.grid(row=2, column=2, sticky=E, padx=5)

    Button(ventana_principal, text="Consultar mensajes recibidos", command=lambda: consultar_mensajes_recibidos(id_usuario)).grid(row=3, column=1, columnspan=2, sticky=W+E, pady=5)

    # Botones a partir de un for loop
    fila_boton = 4
    opciones = ["Cifrar Atbash", "Descifrar Atbash", "Cifrar César", "Descifrar César", "Enviar Mensaje Cifrado César", "Enviar Mensaje Cifrado Atbash"]
    for opcion in opciones:
        Button(ventana_principal, text=opcion, command=lambda opc=opcion: procesar_mensaje(opc, id_usuario, entry_mensaje.get(), entry_clave.get())).grid(row=fila_boton, column=1, columnspan=2, sticky=W+E, pady=5)
        fila_boton += 1

    ventana_principal.mainloop()


def procesar_mensaje(opcion, id_usuario, mensaje, clave):
        resultado = ""
        
        if opcion == "Cifrar Atbash":
            resultado = cifrado_atbash(mensaje)
        elif opcion == "Descifrar Atbash":
            resultado = cifrado_atbash(mensaje)  # Al ser Atbash, cifrar y descifrar es lo mismo
        elif opcion == "Cifrar César":
            if clave.isnumeric():
                resultado = cifrar_string(mensaje, int(clave))
        elif opcion == "Descifrar César":
            if clave.isnumeric():
                resultado = cifrar_string(mensaje, -int(clave))
        elif opcion == "Enviar Mensaje Cifrado César":
            ventana_cesar(id_usuario)
        elif opcion == "Enviar Mensaje Cifrado Atbash":
            ventana_atbash(id_usuario)
        else:
            resultado = "Opción no válida"

        if resultado:
            messagebox.showinfo("Resultado", f"Resultado: {resultado}")

# Llama a la función de la ventana de bienvenida para iniciar la aplicación
mostrar_ventana_bienvenida()
