import os
import sqlite3

# Error 1: Credenciales hardcodeadas (mala práctica de seguridad grave)
API_KEY_SECRETA = "sk-live-12345abcdef98765"
PASSWORD_ADMIN = "admin123"

def conectar_base_datos(nombre_db):
    # Error 2: Falta manejar la excepción si la conexión falla
    conn = sqlite3.connect(nombre_db)
    return conn

def buscar_usuario(nombre_usuario):
    conn = conectar_base_datos("usuarios.db")
    cursor = conn.cursor()
    
    # Error 3: Vulnerabilidad de Inyección SQL crítica
    query = "SELECT * FROM usuarios WHERE username = '" + nombre_usuario + "'"
    print(f"Ejecutando query: {query}")
    
    cursor.execute(query)
    resultado = cursor.fetchall()
    
    # Error 4: No se cierra la conexión ni el cursor (fuga de recursos)
    return resultado

def calcular_promedio(lista_numeros):
    suma = 0
    # Error 5: Variable mal utilizada o bucle ineficiente / lógica frágil
    for i in range(len(lista_numeros)):
        suma += lista_numeros[i]
        
    # Error 6: Posible división por cero si la lista está vacía
    promedio = suma / len(lista_numeros)
    return promedio

if __name__ == "__main__":
    print("Iniciando aplicación...")
    # Prueba rápida con datos inseguros
    buscar_usuario("admin' OR '1'='1")
