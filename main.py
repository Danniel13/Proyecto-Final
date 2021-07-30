"""Importación Librerias"""
import tkinter
from tkinter import *
from tkinter import messagebox
import pymysql
from pymysql import *
from monitoreo import monitor
from datetime import *
import time


"""Definición de función: Menu principal"""

def PantallaPrincipal():
    global form1
    form1=Tk()
    form1.geometry("300x400")
    form1.title("UCI Hospital Santa Clara")
    form1.iconbitmap("ico.ico")
    form1.resizable(False,False)
    

    image=PhotoImage(file="ico.png")
    image=image.subsample(2,2)
    label=Label(image=image)
    label.pack()

    Label (text="UCI Santa Clara", bg="#12A5AC", fg="white", width="300", height="3", font=("arial", 12)).pack()

    Button(text="Registrar Paciente", height="3", width="30", command=RegistroPaciente).pack()

    Button(text="Ingresar", height="3", width="30", command=loginn).pack()

    Button(text="Salir", height="3", width="30", command=exit).pack()

    form1.mainloop()

  
"""Definición de función: Formulario de registro"""

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
    global saturacion
    
   
    fecha_ingreso=StringVar()
    horaingreso=StringVar()
    numerodocumento=int()
    nombres=StringVar()
    apellidos=StringVar()
    sexo=StringVar()
    edad=StringVar()
    sangre=StringVar()
    saturacion=StringVar()

    registro = Toplevel(form1)
    registro.geometry("400x500")
    registro.title("Registro de Pacientes")
    registro.iconbitmap("ico.ico")
    registro.config(bg="#12A5AC")
    registro.resizable(False,False)
    
    """Definición de Fecha y Hora instantanea"""
    today = date.today()
    hora = time.strftime('%H:%M:%S', time.localtime())
    horaingreso= Label (registro, text= today, bg="#12A5AC", fg="white").pack(anchor= E)
    fecha_ingreso= Label (registro, text= hora, bg="#12A5AC", fg="white").pack(anchor= E)
    #datetime.now().time()
    
    Label(registro, text="Datos del Paciente", bg="#12A5AC", fg="white", font=("arial", 16)).pack()
    

    Label(registro, text="Número de indentificación", bg="#12A5AC", fg="white").pack()
    numerodocumento = Entry(registro)
    numerodocumento.pack()

    Label(registro, text="Fecha de ingreso", bg="#12A5AC", fg="white").pack()
    fecha_ingreso = Entry (registro)
    fecha_ingreso.pack()

    Label(registro, text="Hora de Ingreso", bg="#12A5AC", fg="white").pack()
    horaingreso= Entry (registro)
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

    Label(registro, text="Saturación de Oxígeno:", bg="#12A5AC", fg="white").pack()
    saturacion = Entry(registro)
    saturacion.pack()

    Label(registro, text="", bg="#12A5AC", fg="white").pack()
    
    Button(registro, text="Guardar", command=guarda_info).pack()
    Button(registro, text="Salir", command=registro.destroy).pack()


"""Conexión a Base de Datos creada en mysql, y consulta a la base de datos para insertar información"""
def guarda_info():
    savebd=pymysql.connect(
        host="localhost",
        user="root",
        passwd="Pa55w.rd",
        db="proyectofinal"
        
    )
    fcursor=savebd.cursor()
    
    sql= "INSERT INTO registro (numerodocumento, fecha_ingreso, horaingreso, nombres, apellidos, sexo, edad, RH, saturacion) VALUES('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}')".format(numerodocumento.get(), fecha_ingreso.get(), horaingreso.get(), nombres.get(), apellidos.get(), sexo.get(), edad.get(), sangre.get(), saturacion.get())

#Validación de datos guardados satisfactoriamente.#
    try: 
        #Ejecución:
        fcursor.execute(sql)
        savebd.commit()
        messagebox.showinfo(message="Se han guardado los datos", title="Información")
        
    except:
        savebd.rollback()
        messagebox.showinfo(message="No se han podido guardar los datos", title="Error")
    
    savebd.close()



"""Definición de función: Formulario de inicio de sesión"""
def loginn():
    global ingreso
    ingreso = Toplevel(form1)
    ingreso.geometry("400x250")
    ingreso.title("Autenticación de Usuarios")
    ingreso.iconbitmap("candado.ico")
    ingreso.config(bg="#12A5AC")
    ingreso.resizable(False,False)

   
    Label(ingreso, text="Ingrese su nombre ", bg="#12A5AC", fg="white", font=("arial", 16)).pack()
    Label(ingreso, text="de usuario y contraseña ", bg="#12A5AC", fg="white", font=("arial", 16)).pack()
    Label(ingreso, text="", bg="#12A5AC")

    global valida_nameuser
    global valida_claveuser

    valida_nameuser= StringVar()
    valida_claveuser= StringVar()



        


    Label(ingreso, text="Nombre de Usuario:", bg="#12A5AC", fg="white").pack()
    Entry(ingreso, textvariable=valida_nameuser).pack()
    
    Label(ingreso, text="Contraseña:", bg="#12A5AC", fg="white").pack()
    Entry(ingreso, textvariable=valida_claveuser, show="*").pack()   
  
    Label(ingreso, text=" ", bg="#12A5AC").pack()
    Label(ingreso, text=" ", bg="#12A5AC").pack()
    

    Button(ingreso, text="Ingresar", font=("arial", 12), command=inises).pack()
  
"""Conexión con base de datos y consulta contra tabla de autenticación"""

def inises():
    bd=pymysql.connect(
        host="localhost",
        user="root",
        passwd="Pa55w.rd",
        db="proyectofinal"
    )
    
    fcursor2=bd.cursor()
    
    
    fcursor2.execute("SELECT * FROM login where usuario=%s and contrasena=%s",(valida_nameuser.get(), valida_claveuser.get()))
    #Conidicional de comprobación contra la base de datos, y lanzamiendo a formulario adicional#
    if fcursor2.fetchall():
       
        messagebox.showinfo(title="Bienvenido", message="Usuario y clave correcta")
        
        
        monitor()
               
   
    else:
        messagebox.showinfo(title="error", message="No se a podido iniciar sesión")
    

    bd.close()




PantallaPrincipal()


