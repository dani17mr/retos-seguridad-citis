"""
Pruebas del Reto extra. NO necesitas cambiar este archivo.

Cómo correrlo:
    Mac:      python3 probar_reto_extra.py
    Windows:  py probar_reto_extra.py
    IDLE:     abre este archivo y presiona F5
"""

import sys
from pathlib import Path

CARPETA_RETO = Path(__file__).resolve().parent
sys.path.insert(0, str(CARPETA_RETO))

COMPLETO = "COMPLETO"
PENDIENTE = "PENDIENTE"
CON_FALLAS = "CON FALLAS"


def llamar(funcion, *argumentos):
    """Llama a la función del alumno y regresa (estado, valor)."""
    try:
        return "ok", funcion(*argumentos)
    except NotImplementedError:
        return "pendiente", None
    except Exception as error:
        return "error", error


def probar_casos(titulo, funcion, casos):
    print()
    print(titulo)
    fallas = 0
    for entrada, esperado in casos:
        estado, obtenido = llamar(funcion, entrada)
        if estado == "pendiente":
            print("  Todavía hay NotImplementedError en tu función. Escríbela y vuelve a correr.")
            return PENDIENTE
        if estado == "error":
            print("  [ERROR]   con", repr(entrada), "tu función lanzó:", type(obtenido).__name__, "-", obtenido)
            fallas += 1
        elif obtenido == esperado:
            print("  [OK]     ", repr(entrada), "->", repr(obtenido))
        else:
            print("  [FALLA]  ", repr(entrada))
            print("            esperaba:", repr(esperado))
            print("            obtuve:  ", repr(obtenido))
            fallas += 1
    return COMPLETO if fallas == 0 else CON_FALLAS


CASOS_CONTRASENA = [
    ("login usuario=ana password=Cafe2026", "login usuario=ana password=****"),
    ("usuario=ana contraseña=Cafe2026", "usuario=ana contraseña=****"),
    ("PASSWORD=Secreta1", "PASSWORD=****"),
    ("password=abc123 desde la tablet 3", "password=**** desde la tablet 3"),
    ("usuario=ana resultado=ok", "usuario=ana resultado=ok"),
]

CASOS_CORREO = [
    ("ana.lopez@escuela.mx", "a***@escuela.mx"),
    ("jo@uni.mx", "j***@uni.mx"),
    ("sin-arroba", "***"),
    ("@escuela.mx", "***"),
]

ESPERADO_SECRETOS = [
    ("config_app.ini", 9),
    ("config_app.ini", 12),
    ("notas_equipo.txt", 3),
    ("notas_equipo.txt", 5),
    ("pagos_ejemplo.py", 3),
    ("pagos_ejemplo.py", 8),
    ("pagos_ejemplo.py", 9),
]


def nivel3(reto_extra):
    print()
    print("NIVEL 3: buscar_secretos")
    carpeta = CARPETA_RETO / "archivos_ejemplo"
    estado, obtenido = llamar(reto_extra.buscar_secretos, carpeta)
    if estado == "pendiente":
        print("  Todavía hay NotImplementedError en tu función. Escríbela y vuelve a correr.")
        return PENDIENTE
    if estado == "error":
        print("  [ERROR]   tu función lanzó:", type(obtenido).__name__, "-", obtenido)
        if isinstance(obtenido, FileNotFoundError):
            print("            ¿Abriste el archivo con su ruta completa? Usa el objeto 'archivo' de iterdir().")
        return CON_FALLAS
    if not isinstance(obtenido, list):
        print("  [FALLA]   tu función debe regresar una lista y regresó", type(obtenido).__name__)
        return CON_FALLAS

    obtenido_ordenado = sorted(tuple(x) for x in obtenido)
    if obtenido_ordenado == ESPERADO_SECRETOS:
        print("  [OK]      Encontraste las", len(ESPERADO_SECRETOS), "líneas que marca la regla:")
        for nombre, numero in ESPERADO_SECRETOS:
            linea = (carpeta / nombre).read_text(encoding="utf-8").splitlines()[numero - 1]
            print("            " + nombre + ", línea " + str(numero) + ":  " + linea.strip())
        print()
        print("  Ahora discute con tu pareja: ¿cuáles son secretos de verdad y cuáles son falsas alarmas?")
        return COMPLETO

    faltan = [x for x in ESPERADO_SECRETOS if x not in obtenido_ordenado]
    sobran = [x for x in obtenido_ordenado if x not in ESPERADO_SECRETOS]
    print("  [FALLA]   Tu resultado no coincide con la regla.")
    if faltan:
        print("            Te faltan:", faltan)
    if sobran:
        print("            Te sobran:", sobran)
    if len(obtenido_ordenado) != len(set(obtenido_ordenado)):
        print("            Hay líneas repetidas: cuenta cada línea una sola vez (usa any()).")
    if ("notas_equipo.txt", 5) in faltan:
        print("            Si te falta la línea 5 de notas_equipo.txt, abre los archivos con encoding=\"utf-8\".")
    if sobran and all((n, l + 1) in ESPERADO_SECRETOS for n, l in sobran):
        print("            Parece que cuentas desde 0. Usa enumerate(..., start=1).")
    return CON_FALLAS


def main():
    print()
    print("RETO EXTRA: REGISTROS SIN SECRETOS")
    try:
        import reto_extra
    except SyntaxError as error:
        print()
        print("[ERROR] reto_extra.py tiene un error de escritura en la línea", error.lineno)
        if error.text:
            print("       ", error.text.strip())
        print("Revisa paréntesis, comillas, comas y los dos puntos (:) al final de if, for y def.")
        return
    except Exception as error:
        print()
        print("[ERROR] No se pudo cargar reto_extra.py:", type(error).__name__, "-", error)
        return

    resultado1 = probar_casos("NIVEL 1: enmascarar_contrasena", reto_extra.enmascarar_contrasena, CASOS_CONTRASENA)
    resultado2 = probar_casos("NIVEL 2: enmascarar_correo", reto_extra.enmascarar_correo, CASOS_CORREO)
    resultado3 = nivel3(reto_extra)

    print()
    print("RESUMEN")
    print("  Nivel 1:", resultado1)
    print("  Nivel 2:", resultado2)
    print("  Nivel 3:", resultado3)
    print()


main()
