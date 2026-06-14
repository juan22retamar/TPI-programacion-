"""
ordenamiento.py
Módulo encargado de ordenar la lista de países.
"""


def ordenar_paises(paises):
    """
    Ordena los países por nombre, población o superficie,
    de forma ascendente o descendente.
    """
    print("\n--- ORDENAR PAÍSES ---")
    print("¿Por qué campo querés ordenar?")
    print("  1. Nombre")
    print("  2. Población")
    print("  3. Superficie")

    opcion = input("\nElegí una opción (1-3): ").strip()

    if opcion == "1":
        campo = "nombre"
    elif opcion == "2":
        campo = "poblacion"
    elif opcion == "3":
        campo = "superficie"
    else:
        print("[ERROR] Opción inválida.")
        return

    print("\n¿En qué orden?")
    print("  1. Ascendente")
    print("  2. Descendente")

    direccion = input("\nElegí una opción (1-2): ").strip()

    if direccion == "1":
        descendente = False
    elif direccion == "2":
        descendente = True
    else:
        print("[ERROR] Opción inválida.")
        return

    paises_ordenados = sorted(paises, key=lambda p: p[campo], reverse=descendente)

    orden_texto = "descendente" if descendente else "ascendente"
    print(f"\nPaíses ordenados por {campo} ({orden_texto}):")
    for p in paises_ordenados:
        print(f"  - {p['nombre']} | Población: {p['poblacion']:,} | Superficie: {p['superficie']:,} km² | Continente: {p['continente']}")
