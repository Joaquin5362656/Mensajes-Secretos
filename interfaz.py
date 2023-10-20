from tkinter import *
import cifrado_cesar as cesar

def abrir_ventana():
	ventana_de_cifrado = Toplevel()
	ventana_de_cifrado.geometry("300x300")
	ventana_de_cifrado.columnconfigure(0, weight=1)
	ventana_de_cifrado.columnconfigure(1, weight=2)
	ventana_de_cifrado.config(padx=10, pady=10)
	ventana_de_cifrado.resizable(width=False, height=False)

	Label(ventana_de_cifrado, text="Ingrese mensaje:").grid(row=0, column=0, sticky=W, pady=3)
	mensaje = Entry(ventana_de_cifrado).grid(row=0, column=1, sticky=E+W, pady=3)
	Label(ventana_de_cifrado, text="Ingrese clave:").grid(row=1, column=0, sticky=W, pady=3)
	clave = Entry(ventana_de_cifrado).grid(row=1, column=1, sticky=E+W, pady=3)


	Button(ventana_de_cifrado, text="Cifrar mensaje César").grid(row=2, column=0, columnspan=2, sticky=E+W, pady=3)
	Button(ventana_de_cifrado, text="Cifrar mensaje Atbash").grid(row=3, column=0, columnspan=2, sticky=E+W, pady=3)
	Button(ventana_de_cifrado, text="Descifrar mensaje César").grid(row=4, column=0, columnspan=2, sticky=E+W, pady=3)
	Button(ventana_de_cifrado, text="Descifrar mensaje Atbash").grid(row=5, column=0, columnspan=2, sticky=E+W, pady=3)

	return 

root = Tk()
root.geometry("250x300")

Label(root, text="Bienvenido a la aplicación de\nmensajes secretos del grupo CODEO.\nParacontinuar presione continuar, de lo\ncontrario cierre la ventana").place(x=125, y=50, anchor=CENTER)
Button(root, text="Continuar", command=abrir_ventana).place(x=125, y=110, anchor=CENTER)

root.mainloop()

