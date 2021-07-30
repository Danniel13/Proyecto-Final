import pymongo
import pymysql

myclient = pymongo.MongoClient("mongodb+srv://root:<Pa55w.rd>@cluster0.ib5kv.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

mydb = myclient["ProyectoFinal"]

print(myclient.list_database_names())

bd=pymysql.connect(
        host="localhost",
        user="root",
        passwd="Pa55w.rd",
        db="proyectofinal"
    )