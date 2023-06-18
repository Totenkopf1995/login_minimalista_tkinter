import tkinter


ventana = tkinter.Tk()
ventana.title("Login")

# funcion login


def login():
    nombre = nombre_var.get()
    password = password_var.get()

    if nombre == "admin" and password == "admin123":
        mensaje_label.configure(text="Sistema Secreto")
    else:
        mensaje_label.configure(text="Usuario o Password Invalido")


# variables
nombre_var = tkinter.StringVar()
password_var = tkinter.StringVar()


nombre_label = tkinter.Label(
    ventana, text="Usuario", font=("Arial", 18)).pack(padx=20, pady=10)

nombre_entry = tkinter.Entry(ventana, font=(
    "Arial", 16), textvariable=nombre_var).pack(padx=20, pady=10)

password_label = tkinter.Label(
    ventana, text="Password", font=("Arial", 18)).pack(padx=20, pady=10)

password_entry = tkinter.Entry(
    ventana, font=("Arial", 16), textvariable=password_var).pack(padx=20, pady=10)

buton_ingresar = tkinter.Button(
    ventana, text="Ingresar", font=("Arial", 18), command=login).pack(padx=20, pady=10)

mensaje_label = tkinter.Label(
    ventana, text="", font=("Arial", 18))
mensaje_label.pack(padx=20, pady=5)

ventana.mainloop()
