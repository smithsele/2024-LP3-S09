# -*- coding: utf-8 -*-
"""
Created on Mon May 27 16:32:04 2024

@author: Dell
"""
import sqlite3
conexion = sqlite3.connect("bdbiblioteca.db")
cursor = conexion.cursor()
consulta = """ SELECT * 
                FROM LIBRO
                WHERE
                    precio >= 55
                ORDER BY titulo
            """
cursor = conexion.cursor()
cursor.execute(consulta)
libros = cursor.fetchall()
# Acá libros es una lista... entonces utilizamos un for

for libro in libros:
    print(libro)
conexion.close()

