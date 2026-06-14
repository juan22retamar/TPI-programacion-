"""
archivos.py
Módulo encargado de la lectura y escritura del archivo CSV de países.
"""

import csv
import os

NOMBRE_ARCHIVO = "paises.csv"
CAMPOS = ["nombre", "poblacion", "superficie", "continente"]


def leer_paises():
    """
    Lee el archivo CSV y devuelve una lista de diccionarios,
    uno por cada país. Si el archivo no existe, devuelve lista vacía.
    """
    paises = []

    if not os.path.exists(NOMBRE_ARCHIVO):
        print(f"[AVISO] No se encontró el archivo '{NOMBRE_ARCHIVO}'.")
        return paises

    try:
        with open(NOMBRE_ARCHIVO, newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                # Convertir tipos de datos correctamente
                pais = {
                    "nombre": fila["nombre"].strip(),
                    "poblacion": int(fila["poblacion"]),
                    "superficie": int(fila["superficie"]),
                    "continente": fila["continente"].strip()
                }
                paises.append(pais)
    except ValueError as e:
        print(f"[ERROR] Formato inválido en el CSV: {e}")
    except Exception as e:
        print(f"[ERROR] No se pudo leer el archivo: {e}")

    return paises


def guardar_paises(paises):
    """
    Guarda la lista de diccionarios de países en el archivo CSV.
    Sobreescribe el contenido anterior.
    """
    try:
        with open(NOMBRE_ARCHIVO, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=CAMPOS)
            escritor.writeheader()
            escritor.writerows(paises)
        print("[OK] Datos guardados correctamente.")
    except Exception as e:
        print(f"[ERROR] No se pudo guardar el archivo: {e}")
