import tkinter
from tkinter import *
from tkinter import messagebox
import pymysql
from pymysql import *


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
    global numerodocumento
    global fecha_ingreso
    global horaingreso
    global nombres
    global apellidos
    global sexo
    global edad
    global sangre
    global presiónarterial

   
    fecha_ingreso=StringVar()
    horaingreso=StringVar()
    numerodocumento=int()
    nombres=StringVar()
    apellidos=StringVar()
    sexo=StringVar()
    edad=StringVar()
    sangre=StringVar()
    presiónarterial=StringVar()

    registro = Toplevel(form1)
    registro.geometry("800x500")
    registro.title("Registro de Pacientes")
    registro.iconbitmap("ico.ico")
    registro.config(bg="#12A5AC")

    Label(registro, text="Datos del Paciente", bg="#12A5AC", fg="white", font=("arial", 16)).pack()
    

    Label(registro, text="Número de indentificación", bg="#12A5AC", fg="white").pack()
    numerodocumento = Entry(registro)
    numerodocumento.pack()

    Label(registro, text="Fecha de ingreso", bg="#12A5AC", fg="white").pack()
    fecha_ingreso = Entry(registro)
    fecha_ingreso.pack()

    Label(registro, text="Hora de Ingreso", bg="#12A5AC", fg="white").pack()
    horaingreso = Entry(registro)
    horaingreso.pack()

    Label(registro, text="Nombres: ", bg="#12A5AC", fg="white").pack()
    nombres = Entry(registro)
    nombres.pack()

    Label(registro, text="Apellidos: ", bg="#12A5AC", fg="white").pack()
    apellidos = Entry(registro)
    apellidos.pack()

    Label(registro, text="Sexo: ", bg="#12A5AC", fg="white").pack()
    sexo = Entry(registro)
    sexo.pack()

    Label(registro, text="Edad: ", bg="#12A5AC", fg="white").pack()
    edad = Entry(registro)
    edad.pack()

    Label(registro, text="RH: ", bg="#12A5AC", fg="white").pack()
    sangre = Entry(registro)
    sangre.pack()

    Label(registro, text="Presión Arterial ", bg="#12A5AC", fg="white").pack()
    presiónarterial = Entry(registro)
    presiónarterial.pack()


    Button(registro, text="Guardar", command=guarda_info).pack()

def guarda_info():
    savebd=pymysql.connect(
        host="localhost",
        user="root",
        passwd="Pa55w.rd",
        db="proyectofinal"
    )
    fcursor=savebd.cursor()
    
    sql= "INSERT INTO registro (numerodocumento, fecha_ingreso, horaingreso, nombres, apellidos, sexo, edad, RH, presionarterial) VALUES('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}')".format(numerodocumento.get(), fecha_ingreso.get(), horaingreso.get(), nombres.get(), apellidos.get(), sexo.get(), edad.get(), sangre.get(), presiónarterial.get())


    try: 
        #Ejecución:
        fcursor.execute(sql)
        savebd.commit()
        messagebox.showinfo(message="Se han guardado los datos", title="Información")

    except:
        savebd.rollback()
        messagebox.showinfo(message="No se han podido guardar los datos", title="Error")
    
    savebd.close()



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

    valida_nameuser= str()
    valida_claveuser= str()


#Validar variables globales que se estan usando para adicion de usuario y autenticació#
    
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


    Button(ingreso, text="Ingresar", font=("arial", 12), command=inises).pack()
  

def inises():
    bd=pymysql.connect(
        host="localhost",
        user="root",
        passwd="Pa55w.rd",
        db="proyectofinal"
    )
    fcursor=bd.cursor()
    
    fcursor.execute("SELECT contrasena FROM login WHERE usuario='"+valida_nameuser+"' and contrasena ='"+valida_claveuser+"'")
    if fcursor.fetchall():
        messagebox.showinfo(title="Inicio de sesión correcto", message="Usuario y clave correcta")
        
    else:
        messagebox.showinfo(title="error", message="No se a podido iniciar sesión")
   
  
   
    bd.close()





PantallaPrincipal()
