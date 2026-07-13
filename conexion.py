# 1_conexion_db.py
# Propósito: Conectar Python con la base de datos MySQL en XAMPP

import mysql.connector
from mysql.connector import Error

def conectar():
    """
    Establece conexión con la base de datos 'biblioteca' en XAMPP
    Devuelve el objeto de conexión o None si hay error
    """
    try:
        conexion = mysql.connector.connect(
            host="localhost",           # Dirección del servidor (siempre es así en XAMPP)
            user="root",                # Usuario predeterminado de XAMPP
            password="",                # Contraseña predeterminada: vacía
            database="biblioteca"       # Nombre de la base que creaste
        )
        if conexion.is_connected():
            return conexion
    except Error as e:
        print(f"❌ Error al conectar a la base de datos: {e}")
        return None