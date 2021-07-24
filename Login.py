import tkinter
from tkinter import *
from tkinter import messagebox


def PantallaPrincipal():
    global form1
    form1=Tk()
    form1.geometry("300x400")
    form1.title("UCI Hospital Santa Clara")
    form1.iconbitmap("ico.ico")


    image=PhotoImage(file="ico.png")
    image=image.subsample(2,2)
    label=Label(image=image)
    label.pack()

    Label (text="UCI Santa Clara", bg="#12A5AC", fg="white", width="300", height="3", font=("arial", 12)).pack()

    Button(text="Registrar Paciente", height="3", width="30", command=RegistroPaciente).pack()

    Button(text="Ingresar", height="3", width="30", command=login).pack()

    Button(text="Salir", height="3", width="30", command=exit).pack()

    form1.mainloop()


def RegistroPaciente():
    global registro
    registro = Toplevel(form1)
    registro.geometry("400x250")
    registro.title("Registro de Pacientes")
    registro.iconbitmap("ico.ico")

    Label(registro, text="Datos de paciente").pack()
    Label(registro, text="").pack()

   


def login():
    global ingreso
    ingreso = Toplevel(form1)
    ingreso.geometry("400x250")
    ingreso.title("Autenticación de Usuarios")
    ingreso.iconbitmap("candado.ico")
    ingreso.config(bg="#12A5AC")
    

   
    Label(ingreso, text="Ingrese su nombre ", bg="#12A5AC", fg="white", font=("arial", 16)).pack()
    Label(ingreso, text="de usuario y contraseña ", bg="#12A5AC", fg="white", font=("arial", 16)).pack()
    Label(ingreso, text="", bg="#12A5AC")

    global valida_nameuser
    global valida_claveuser

    valida_nameuser=StringVar()
    valida_claveuser=StringVar()

    global name_user_intro
    global clave_user_intro

    Label(ingreso, text="Nombre de Usuario:", bg="#12A5AC", fg="white").pack()
    name_user_intro = Entry(ingreso, textvariable=valida_nameuser)
    name_user_intro.pack()
    

    Label(ingreso, text="Contraseña:", bg="#12A5AC", fg="white").pack()
    clave_user_intro = Entry(ingreso, textvariable=valida_claveuser)
    clave_user_intro.pack()
    Label(ingreso, text=" ", bg="#12A5AC").pack()
    Label(ingreso, text=" ", bg="#12A5AC").pack()


    Button(ingreso, text="Ingresar", font=("arial", 12)).pack()
  

   



PantallaPrincipal()