from tkinter import Toplevel
from tkinter import *
from tkinter import messagebox
import csv

def mostrar_ventana_ingreso():
    ventana_ingreso = Toplevel()
    ventana_ingreso.title("Identificación para acceso")
    ventana_ingreso.geometry("300x150")

    Label(ventana_ingreso, text="Ingrese su usuario:").pack(pady=10)
    entry_usuario_ingreso = Entry(ventana_ingreso)
    entry_usuario_ingreso.pack(pady=5)

    Label(ventana_ingreso, text="Ingrese su clave:").pack(pady=10)
    entry_clave_ingreso = Entry(ventana_ingreso, show="*")
    entry_clave_ingreso.pack(pady=5)

    Button(ventana_ingreso, text="Ingresar", command=lambda: validar_ingreso(entry_usuario_ingreso, entry_clave_ingreso)).pack(pady=10)

def validar_ingreso(entry_usuario_ingreso, entry_clave_ingreso):
    id_usuario_ingreso = entry_usuario_ingreso.get()
    clave_ingreso = entry_clave_ingreso.get()

    # Lógica de validación del ingreso del usuario
    # Puedes cargar el archivo CSV existente y verificar si el ID y la clave coinciden

    # Ejemplo simplificado:
    with open('usuarios.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] == id_usuario_ingreso and row[1] == clave_ingreso:
                messagebox.showinfo("Éxito", "Ingreso exitoso")
                return

    messagebox.showinfo("Error", "Identificador inexistente o clave errónea\nSi no estás registrado, regístrate previamente\no si olvidaste la clave, presiona el botón recuperar clave.")
