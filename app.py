
import csv
import sqlite3

def cargarArchivo():

    a= open('medals_total.csv', mode='r', encoding='utf-8-sig')
    next(a,None)
    lectura = csv.reader(a, delimiter=';')
    return lectura
        

def guardarArchivo(archivo):
    try:
        with sqlite3.connect('BD.db') as bd:
            
            cursor = bd.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS BD(
                                        PAIS TEXT NOT NULL,
                                        ORO INTEGER NOT NULL,
                                        PLATA INTEGER NOT NULL,
                                        BRONCE INTEGER NOT NULL,
                                        TOTAL INTEGER NOT NULL,
                                        PUESTO INTEGER NOT NULL
                                                            ) """)
            
            for row in archivo:
                cursor.execute("INSERT INTO BD VALUES (?,?,?,?,?,?)",(row[1],row[2],row[3],row[4],row[5],row[6]))
            bd.commit()
            print('Archivo guardado correctamente')
        
    except sqlite3.OperationalError as error:
	    print("Error al abrir:", error)


def descargar():
    try:
        with sqlite3.connect('BD.db') as bd:
            cursor = bd.cursor()
            cursor.execute("SELECT * FROM BD")
            data = cursor.fetchall()

            encabezado= ['PAIS','ORO','PLATA','BRONCE','TOTAL','PUESTO']
            nuevo= open('nuevoArchivo.csv' , mode='w', encoding='utf-8-sig')
            escritura = csv.writer(nuevo, delimiter=';')

            for fila in data:
                escritura.writerow(fila)

    except sqlite3.OperationalError as error:
	    print("Error al abrir:", error)



if __name__ == '__main__':

    archivo = cargarArchivo()
    guardarArchivo(archivo)

    descargar()

