"""
gestor.py
Módulo encargado de agregar y actualizar países en la lista.
"""

from archivos import guardar_paises


def agregar_pais(paises):
    """
    Solicita los datos de un nuevo país por consola y lo agrega a la lista.
    No se permiten campos vacíos.
    """
    print("\n--- AGREGAR PAÍS ---")

    nombre = input("Nombre del país: ").strip()
    if not nombre:
        print("[ERROR] El nombre no puede estar vacío.")
        return

    # Verificar que no exista ya un país con ese nombre
    for p in paises:
        if p["nombre"].lower() == nombre.lower():
            print(f"[ERROR] Ya existe un país con el nombre '{nombre}'.")
            return

    try:
        poblacion = int(input("Población: ").strip())
        superficie = int(input("Superficie en km²: ").strip())
    except ValueError:
        print("[ERROR] Población y superficie deben ser números enteros.")
        return

    continente = input("Continente: ").strip()
    if not continente:
        print("[ERROR] El continente no puede estar vacío.")
        return

    pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    paises.append(pais)
    guardar_paises(paises)
    print(f"[OK] País '{nombre}' agregado correctamente.")


def actualizar_pais(paises):
    """
    Busca un país por nombre y permite actualizar su población y superficie.
    """
    print("\n--- ACTUALIZAR PAÍS ---")

    nombre = input("Nombre del país a actualizar: ").strip()
    if not nombre:
        print("[ERROR] El nombre no puede estar vacío.")
        return

    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            try:
                poblacion = int(input(f"Nueva población (actual: {pais['poblacion']}): ").strip())
                superficie = int(input(f"Nueva superficie (actual: {pais['superficie']}): ").strip())
            except ValueError:
                print("[ERROR] Población y superficie deben ser números enteros.")
                return

            pais["poblacion"] = poblacion
            pais["superficie"] = superficie
            guardar_paises(paises)
            print(f"[OK] País '{nombre}' actualizado correctamente.")
            return

    print(f"[ERROR] No se encontró ningún país con el nombre '{nombre}'.")
