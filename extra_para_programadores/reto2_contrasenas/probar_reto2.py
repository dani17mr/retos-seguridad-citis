"""
Pruebas del Reto 2. NO necesitas cambiar este archivo.

Cómo correrlo:
    Mac:      python3 probar_reto2.py
    Windows:  py probar_reto2.py
    IDLE:     abre este archivo y presiona F5
"""

import hashlib
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

COMPLETO = "COMPLETO"
PENDIENTE = "PENDIENTE"
CON_FALLAS = "CON FALLAS"

CONTRASENA = "Cafeteria2026"


def llamar(funcion, *argumentos):
    """Llama a la función del alumno y regresa (estado, valor)."""
    try:
        return "ok", funcion(*argumentos)
    except NotImplementedError:
        return "pendiente", None
    except NameError as error:
        if "___" in str(error):
            return "pendiente", None
        return "error", error
    except Exception as error:
        return "error", error


def corto(texto):
    return texto if len(texto) <= 40 else texto[:40] + "..."


def nivel1(reto2):
    print()
    print("NIVEL 1: guardar_seguro")

    print("  Observa primero cómo guarda MD5 la misma contraseña dos veces:")
    print("     MD5 #1:", reto2.guardar_md5(CONTRASENA))
    print("     MD5 #2:", reto2.guardar_md5(CONTRASENA))
    print("     Son idénticos. Quien vea dos hashes iguales sabe que son la misma contraseña.")
    print()

    estado, guardado1 = llamar(reto2.guardar_seguro, CONTRASENA)
    if estado == "pendiente":
        print("  Todavía hay ___ en guardar_seguro. Complétala y vuelve a correr.")
        return PENDIENTE
    if estado == "error":
        print("  [ERROR]  guardar_seguro lanzó:", type(guardado1).__name__, "-", guardado1)
        print("           Revisa que copiaste bien las pistas de los Pasos 1 y 2.")
        return CON_FALLAS
    if not isinstance(guardado1, str):
        print("  [FALLA]  guardar_seguro debe regresar un texto y regresó", repr(guardado1))
        return CON_FALLAS

    fallas = 0
    if re.fullmatch(r"[0-9a-f]{32}\$[0-9a-f]{64}", guardado1):
        print("  [OK]     El formato es sal$hash: 32 caracteres de sal y 64 de hash.")
    else:
        print("  [FALLA]  El formato debe ser sal$hash (32 + 1 + 64 caracteres). Obtuve:", corto(guardado1))
        fallas += 1

    if CONTRASENA in guardado1:
        print("  [FALLA]  ¡La contraseña aparece tal cual en lo que guardaste!")
        fallas += 1
    else:
        print("  [OK]     La contraseña original no aparece en lo guardado.")

    estado, guardado2 = llamar(reto2.guardar_seguro, CONTRASENA)
    print("     Seguro #1:", corto(guardado1))
    print("     Seguro #2:", corto(str(guardado2)))
    if estado == "ok" and guardado2 != guardado1:
        print("  [OK]     La misma contraseña quedó guardada distinta las dos veces: la sal funciona.")
    else:
        print("  [FALLA]  La misma contraseña quedó igual las dos veces. ¿Usaste os.urandom(16) para la sal?")
        fallas += 1

    if fallas == 0 and len(guardado1.split("$")) == 2:
        sal_hex, hash_hex = guardado1.split("$")
        esperado = hashlib.pbkdf2_hmac("sha256", CONTRASENA.encode("utf-8"),
                                       bytes.fromhex(sal_hex), reto2.ITERACIONES).hex()
        if esperado == hash_hex:
            print("  [OK]     El hash corresponde a PBKDF2 con", f"{reto2.ITERACIONES:,}", "iteraciones.")
        else:
            print("  [FALLA]  El hash no corresponde a PBKDF2 con la sal guardada. Revisa el Paso 2.")
            fallas += 1

    return COMPLETO if fallas == 0 else CON_FALLAS


def nivel2(reto2):
    print()
    print("NIVEL 2: verificar")
    guardado = reto2.guardar_seguro(CONTRASENA)

    sal = bytes.fromhex("000102030405060708090a0b0c0d0e0f")
    guardado_por_el_ponente = sal.hex() + "$" + hashlib.pbkdf2_hmac(
        "sha256", CONTRASENA.encode("utf-8"), sal, reto2.ITERACIONES).hex()

    casos = [
        ((CONTRASENA, guardado), True, "la contraseña correcta"),
        (("cafeteria2026", guardado), False, "igual pero con c minúscula"),
        ((CONTRASENA + " ", guardado), False, "con un espacio al final"),
        (("", guardado), False, "contraseña vacía"),
        ((CONTRASENA, guardado_por_el_ponente), True, "un registro guardado por otro programa con PBKDF2"),
    ]

    fallas = 0
    for argumentos, esperado, explicacion in casos:
        estado, obtenido = llamar(reto2.verificar, *argumentos)
        if estado == "pendiente":
            print("  Todavía hay NotImplementedError en verificar. Escríbela siguiendo los 4 pasos.")
            return PENDIENTE
        if estado == "error":
            print("  [ERROR]  con", explicacion + ", verificar lanzó:", type(obtenido).__name__, "-", obtenido)
            fallas += 1
        elif not isinstance(obtenido, bool):
            print("  [FALLA]  con", explicacion + ", verificar regresó", repr(obtenido), "y debe regresar True o False.")
            fallas += 1
        elif obtenido == esperado:
            print("  [OK]     ", explicacion, "->", obtenido)
        else:
            print("  [FALLA]  ", explicacion, ": esperaba", esperado, "y tu función dio", obtenido)
            fallas += 1

    if fallas == 0:
        print("  Comenta con tu pareja: ¿por qué se usa hmac.compare_digest y no == ?")
    return COMPLETO if fallas == 0 else CON_FALLAS


def main():
    print()
    print("RETO 2: GUARDAR CONTRASEÑAS")
    print("(Tarda unos segundos: el algoritmo es lento a propósito.)")
    try:
        import reto2
    except SyntaxError as error:
        print()
        print("[ERROR] reto2.py tiene un error de escritura en la línea", error.lineno)
        if error.text:
            print("       ", error.text.strip())
        print("Revisa paréntesis, comillas, comas y los dos puntos (:) al final de if, for y def.")
        return
    except Exception as error:
        print()
        print("[ERROR] No se pudo cargar reto2.py:", type(error).__name__, "-", error)
        return

    resultado1 = nivel1(reto2)
    if resultado1 == COMPLETO:
        resultado2 = nivel2(reto2)
    else:
        print()
        print("NIVEL 2: termina primero el Nivel 1.")
        resultado2 = PENDIENTE

    print()
    print("RESUMEN")
    print("  Nivel 1:", resultado1)
    print("  Nivel 2:", resultado2)
    print("  Nivel 3: corre  medir_tiempos.py  (Mac: python3 medir_tiempos.py / Windows: py medir_tiempos.py)")
    print()
    if resultado1 != COMPLETO:
        print("Siguiente paso: corrige el Nivel 1 y vuelve a correr este archivo.")
    elif resultado2 != COMPLETO:
        print("Muy bien. Siguiente paso: el Nivel 2.")
    else:
        print("Muy bien. Siguiente paso: el Nivel 3 en medir_tiempos.py.")
    print()


main()
