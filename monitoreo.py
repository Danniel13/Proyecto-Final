"""Definición de librerias"""
import tkinter
from tkinter import *
from tkinter import messagebox
import pymysql
from pymysql import *
from pymysql.cursors import Cursor
from random import *

"""Definición de función: Monitoreo pacientes"""
def monitor():
    global form_monitor
    form_monitor=Tk()
    form_monitor.geometry("500x500")
    form_monitor.title("Monitoreo Pacientes UCI")
    form_monitor.iconbitmap("ico.ico")
    form_monitor.resizable(False,False)
    form_monitor.config(bg="#12A5AC")
    
    


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

   


    Label(form_monitor, text="Número de indentificación", bg="#12A5AC", fg="white").pack()
    numerodocumento = Entry(form_monitor)
    numerodocumento.pack()

    Label(form_monitor, text="Fecha de ingreso", bg="#12A5AC", fg="white").pack()
    fecha_ingreso = Entry (form_monitor)
    fecha_ingreso.pack()

    Label(form_monitor, text="Nombres: ", bg="#12A5AC", fg="white").pack()
    nombres = Entry(form_monitor)
    nombres.pack()

    Label(form_monitor, text="Apellidos: ", bg="#12A5AC", fg="white").pack()
    apellidos = Entry(form_monitor)
    apellidos.pack()

    Label(form_monitor, text="Sexo: ", bg="#12A5AC", fg="white").pack()
    sexo = Entry(form_monitor)
    sexo.pack()

    Label(form_monitor, text="Edad: ", bg="#12A5AC", fg="white").pack()
    edad = Entry(form_monitor)
    edad.pack()

    Label(form_monitor, text="RH: ", bg="#12A5AC", fg="white").pack()
    sangre = Entry(form_monitor)
    sangre.pack()

    Label(form_monitor, text="Saturación de Oxígeno:", bg="#12A5AC", fg="white").pack()
    saturacion = Entry(form_monitor)
    saturacion.pack()

    Label(form_monitor, text="", bg="#12A5AC", fg="white").pack()
    
    Button(form_monitor, text="Consultar", command=consulta_datos).pack()
    Button(form_monitor, text="Salir", command=form_monitor.destroy).pack()

 

"""Definición de función: Consulta de información en Base de datos"""

def consulta_datos():
    #Condicional de busqueda de datos a partir del número de documento del paciente#
    if(numerodocumento.get()==""):
        messagebox.showinfo= "Actualizando registros..."
    else:
        bd=pymysql.connect( #conexión a la Base de datos#
        host="localhost",
        user="root",
        passwd="Pa55w.rd",
        db="proyectofinal"
        
    )
    #Consulta a la base de datos para traer información#
        cursor= bd.cursor()
        cursor.execute("SELECT * FROM registro WHERE numerodocumento='"+numerodocumento.get()+"'")
        rows= cursor.fetchall()
        for row in rows:
            fecha_ingreso.insert(0, row[1])
            nombres.insert(0, row[3])
            apellidos.insert(0, row[4])
            sexo.insert(0, row[5])
            edad.insert(0, row[6])                             
            sangre.insert(0, row[7])
        
        bd.close()

  

if __name__ == "__main__":
    pass
