"""
main.py
Módulo principal. Muestra el menú y coordina el resto de los módulos.
"""

from archivos import leer_paises
from gestor import agregar_pais, actualizar_pais
from busqueda import buscar_por_nombre, filtrar_por_continente, filtrar_por_poblacion, filtrar_por_superficie
from ordenamiento import ordenar_paises
from estadisticas import mostrar_estadisticas


def mostrar_menu():
    """
    Muestra el menú principal en consola.
    """
    print("\n=============================")
    print("   GESTIÓN DE PAÍSES - UTN   ")
    print("=============================")
    print("  1. Agregar país")
    print("  2. Actualizar país")
    print("  3. Buscar país por nombre")
    print("  4. Filtrar países")
    print("  5. Ordenar países")
    print("  6. Ver estadísticas")
    print("  0. Salir")
    print("=============================")


def menu_filtros(paises):
    """
    Muestra el submenú de filtros.
    """
    print("\n--- FILTRAR PAÍSES ---")
    print("  1. Por continente")
    print("  2. Por rango de población")
    print("  3. Por rango de superficie")

    opcion = input("\nElegí una opción (1-3): ").strip()

    if opcion == "1":
        filtrar_por_continente(paises)
    elif opcion == "2":
        filtrar_por_poblacion(paises)
    elif opcion == "3":
        filtrar_por_superficie(paises)
    else:
        print("[ERROR] Opción inválida.")


def main():
    """
    Función principal. Carga los datos y ejecuta el menú en bucle.
    """
    paises = leer_paises()

    while True:
        mostrar_menu()
        opcion = input("Elegí una opción: ").strip()

        if opcion == "1":
            agregar_pais(paises)
        elif opcion == "2":
            actualizar_pais(paises)
        elif opcion == "3":
            buscar_por_nombre(paises)
        elif opcion == "4":
            menu_filtros(paises)
        elif opcion == "5":
            ordenar_paises(paises)
        elif opcion == "6":
            mostrar_estadisticas(paises)
        elif opcion == "0":
            print("\n¡Hasta luego!")
            break
        else:
            print("[ERROR] Opción inválida. Intentá de nuevo.")


if __name__ == "__main__":
    main()
