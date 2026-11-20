"""
Pruebas del Reto 1. NO necesitas cambiar este archivo.

Cómo correrlo:
    Mac:      python3 probar_reto1.py
    Windows:  py probar_reto1.py
    IDLE:     abre este archivo y presiona F5
"""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

COMPLETO = "COMPLETO"
PENDIENTE = "PENDIENTE"
CON_FALLAS = "CON FALLAS"


def mostrar(texto):
    """Muestra un texto entre comillas, con los caracteres invisibles a la vista."""
    if len(texto) > 15:
        return repr(texto[:8] + "...") + " (" + str(len(texto)) + " caracteres)"
    return repr(texto)


def llamar(funcion, entrada):
    """Llama a la función del alumno y regresa (estado, valor)."""
    try:
        return "ok", funcion(entrada)
    except NotImplementedError:
        return "pendiente", None
    except NameError as error:
        if "___" in str(error):
            return "pendiente", None
        return "error", error
    except Exception as error:
        return "error", error


def probar_casos(titulo, funcion, casos):
    print()
    print(titulo)
    fallas = 0
    for entrada, esperado, explicacion in casos:
        estado, obtenido = llamar(funcion, entrada)
        if estado == "pendiente":
            print("  Todavía hay ___ o NotImplementedError en tu función. Complétala y vuelve a correr.")
            return PENDIENTE
        if estado == "error":
            print("  [ERROR]  con", mostrar(entrada), "tu función lanzó:", type(obtenido).__name__, "-", obtenido)
            fallas += 1
            continue
        if not isinstance(obtenido, bool):
            print("  [FALLA]  con", mostrar(entrada), "tu función regresó", repr(obtenido),
                  "y debe regresar True o False.")
            if obtenido is None:
                print("           ¿Olvidaste escribir return en algún camino?")
            fallas += 1
            continue
        if obtenido == esperado:
            print("  [OK]     ", mostrar(entrada), "->", obtenido, "  (" + explicacion + ")")
        else:
            print("  [FALLA]  ", mostrar(entrada), ": esperaba", esperado, "y tu función dio", obtenido,
                  "  (" + explicacion + ")")
            fallas += 1
    return COMPLETO if fallas == 0 else CON_FALLAS


CASOS_USUARIO = [
    ("ana", True, "3 caracteres, solo letras"),
    ("jose_luis", True, "letras y guion bajo"),
    ("Maria2005", True, "mayúsculas, minúsculas y números"),
    ("abcdefghij0123456789", True, "exactamente 20 caracteres"),
    ("", False, "está vacío"),
    ("ab", False, "solo tiene 2 caracteres"),
    ("abcdefghij0123456789_", False, "tiene 21 caracteres, uno de más"),
    ("ana lopez", False, "tiene un espacio"),
    ("jose.luis", False, "tiene un punto"),
    ("ana!", False, "tiene un signo de admiración"),
    ("maría", False, "tiene una letra con acento"),
    ("ana\n", False, "termina con un salto de línea invisible"),
]

CASOS_IP = [
    ("192.168.1.10", True, "IPv4 de una red privada"),
    ("8.8.8.8", True, "IPv4 pública"),
    ("2001:db8::1", True, "IPv6"),
    ("999.1.1.1", False, "999 no es válido: cada número va de 0 a 255"),
    ("192.168.1", False, "le falta un número"),
    ("localhost", False, "es un nombre, no una IP"),
    ("", False, "está vacío"),
    ("8.8.8.8 ", False, "tiene un espacio al final"),
    ("8.8.8.8 y algo más", False, "trae texto extra después de la IP"),
]


def cumple_regla(texto):
    """La regla de CafeApp, escrita por el ponente, para revisar los casos del Nivel 2."""
    return isinstance(texto, str) and re.fullmatch(r"[A-Za-z0-9_]{3,20}", texto) is not None


def probar_nivel2(reto1):
    print()
    print("NIVEL 2: tus propios casos de prueba")
    validos = getattr(reto1, "MIS_VALIDOS", [])
    invalidos = getattr(reto1, "MIS_INVALIDOS", [])
    ya_usados = {caso[0] for caso in CASOS_USUARIO}
    nuevos_validos = [t for t in validos if t not in ya_usados]
    nuevos_invalidos = [t for t in invalidos if t not in ya_usados]

    if len(nuevos_validos) < 3 or len(nuevos_invalidos) < 3:
        print("  Escribe al menos 3 nombres NUEVOS en MIS_VALIDOS y 3 en MIS_INVALIDOS.")
        print("  Llevas", len(nuevos_validos), "válidos y", len(nuevos_invalidos), "inválidos nuevos.")
        return PENDIENTE

    fallas = 0
    for lista, esperado, nombre_lista in ((validos, True, "MIS_VALIDOS"), (invalidos, False, "MIS_INVALIDOS")):
        for texto in lista:
            if not isinstance(texto, str):
                print("  [REVISA] ", repr(texto), "en", nombre_lista, "no es texto. Ponlo entre comillas.")
                fallas += 1
                continue
            if cumple_regla(texto) != esperado:
                otra = "MIS_INVALIDOS" if esperado else "MIS_VALIDOS"
                print("  [REVISA] ", mostrar(texto), "está en", nombre_lista,
                      "pero según la regla debería ir en", otra + ".")
                fallas += 1
                continue
            estado, obtenido = llamar(reto1.es_usuario_valido, texto)
            if estado != "ok" or obtenido != esperado:
                print("  [FALLA]  ", mostrar(texto), ": la regla dice", esperado, "y tu función dio", obtenido)
                fallas += 1
            else:
                print("  [OK]     ", mostrar(texto), "->", obtenido)
    if fallas == 0:
        print("  No olvides responder la pregunta del Nivel 2 en reto1.py y comentarla con tu pareja.")
    return COMPLETO if fallas == 0 else CON_FALLAS


def main():
    print()
    print("RETO 1: VALIDAR ENTRADAS")
    try:
        import reto1
    except SyntaxError as error:
        print()
        print("[ERROR] reto1.py tiene un error de escritura en la línea", error.lineno)
        if error.text:
            print("       ", error.text.strip())
        print("Revisa paréntesis, comillas, comas y los dos puntos (:) al final de if, for y def.")
        return
    except Exception as error:
        print()
        print("[ERROR] No se pudo cargar reto1.py:", type(error).__name__, "-", error)
        return

    nivel1 = probar_casos("NIVEL 1: es_usuario_valido", reto1.es_usuario_valido, CASOS_USUARIO)

    if nivel1 == COMPLETO:
        nivel2 = probar_nivel2(reto1)
    else:
        print()
        print("NIVEL 2: termina primero el Nivel 1.")
        nivel2 = PENDIENTE

    nivel3 = probar_casos("NIVEL 3: es_ip_valida", reto1.es_ip_valida, CASOS_IP)

    print()
    print("RESUMEN")
    print("  Nivel 1:", nivel1)
    print("  Nivel 2:", nivel2)
    print("  Nivel 3:", nivel3)
    print()
    if nivel1 != COMPLETO:
        print("Siguiente paso: corrige el Nivel 1 y vuelve a correr este archivo.")
    elif nivel2 != COMPLETO:
        print("Muy bien. Siguiente paso: el Nivel 2.")
    elif nivel3 != COMPLETO:
        print("Muy bien. Siguiente paso: el Nivel 3.")
    else:
        print("Reto 1 completo. Pasa al Reto 2 (carpeta reto2_contrasenas).")
    print()


main()
