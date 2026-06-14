"""
busqueda.py
Módulo encargado de buscar y filtrar países.
"""


def buscar_por_nombre(paises):
    """
    Busca países por nombre, coincidencia parcial o exacta.
    """
    print("\n--- BUSCAR PAÍS POR NOMBRE ---")

    nombre = input("Ingresá el nombre o parte del nombre: ").strip()
    if not nombre:
        print("[ERROR] El nombre no puede estar vacío.")
        return

    resultados = [p for p in paises if nombre.lower() in p["nombre"].lower()]

    if not resultados:
        print(f"[AVISO] No se encontraron países con '{nombre}'.")
        return

    print(f"\nSe encontraron {len(resultados)} resultado/s:")
    for p in resultados:
        print(f"  - {p['nombre']} | Población: {p['poblacion']:,} | Superficie: {p['superficie']:,} km² | Continente: {p['continente']}")


def filtrar_por_continente(paises):
    """
    Filtra países por continente.
    """
    print("\n--- FILTRAR POR CONTINENTE ---")

    continente = input("Ingresá el continente: ").strip()
    if not continente:
        print("[ERROR] El continente no puede estar vacío.")
        return

    resultados = [p for p in paises if p["continente"].lower() == continente.lower()]

    if not resultados:
        print(f"[AVISO] No se encontraron países en '{continente}'.")
        return

    print(f"\nPaíses en {continente}:")
    for p in resultados:
        print(f"  - {p['nombre']} | Población: {p['poblacion']:,} | Superficie: {p['superficie']:,} km²")


def filtrar_por_poblacion(paises):
    """
    Filtra países por rango de población.
    """
    print("\n--- FILTRAR POR RANGO DE POBLACIÓN ---")

    try:
        minimo = int(input("Población mínima: ").strip())
        maximo = int(input("Población máxima: ").strip())
    except ValueError:
        print("[ERROR] Ingresá números enteros válidos.")
        return

    if minimo > maximo:
        print("[ERROR] El mínimo no puede ser mayor al máximo.")
        return

    resultados = [p for p in paises if minimo <= p["poblacion"] <= maximo]

    if not resultados:
        print(f"[AVISO] No se encontraron países en ese rango de población.")
        return

    print(f"\nPaíses con población entre {minimo:,} y {maximo:,}:")
    for p in resultados:
        print(f"  - {p['nombre']} | Población: {p['poblacion']:,} | Continente: {p['continente']}")


def filtrar_por_superficie(paises):
    """
    Filtra países por rango de superficie en km².
    """
    print("\n--- FILTRAR POR RANGO DE SUPERFICIE ---")

    try:
        minimo = int(input("Superficie mínima (km²): ").strip())
        maximo = int(input("Superficie máxima (km²): ").strip())
    except ValueError:
        print("[ERROR] Ingresá números enteros válidos.")
        return

    if minimo > maximo:
        print("[ERROR] El mínimo no puede ser mayor al máximo.")
        return

    resultados = [p for p in paises if minimo <= p["superficie"] <= maximo]

    if not resultados:
        print(f"[AVISO] No se encontraron países en ese rango de superficie.")
        return

    print(f"\nPaíses con superficie entre {minimo:,} y {maximo:,} km²:")
    for p in resultados:
        print(f"  - {p['nombre']} | Superficie: {p['superficie']:,} km² | Continente: {p['continente']}")
