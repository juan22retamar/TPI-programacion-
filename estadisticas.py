"""
estadisticas.py
Módulo encargado de calcular y mostrar estadísticas de los países.
"""


def mostrar_estadisticas(paises):
    """
    Muestra estadísticas generales del dataset de países.
    """
    print("\n--- ESTADÍSTICAS ---")

    if not paises:
        print("[AVISO] No hay países cargados.")
        return

    # País con mayor y menor población
    mayor_poblacion = max(paises, key=lambda p: p["poblacion"])
    menor_poblacion = min(paises, key=lambda p: p["poblacion"])

    # Promedios
    promedio_poblacion = sum(p["poblacion"] for p in paises) / len(paises)
    promedio_superficie = sum(p["superficie"] for p in paises) / len(paises)

    # Cantidad de países por continente
    por_continente = {}
    for p in paises:
        continente = p["continente"]
        if continente in por_continente:
            por_continente[continente] += 1
        else:
            por_continente[continente] = 1

    print(f"\nPaís con mayor población: {mayor_poblacion['nombre']} ({mayor_poblacion['poblacion']:,} hab.)")
    print(f"País con menor población: {menor_poblacion['nombre']} ({menor_poblacion['poblacion']:,} hab.)")
    print(f"\nPromedio de población:  {promedio_poblacion:,.0f} hab.")
    print(f"Promedio de superficie: {promedio_superficie:,.0f} km²")

    print("\nCantidad de países por continente:")
    for continente, cantidad in por_continente.items():
        print(f"  - {continente}: {cantidad} país/es")
