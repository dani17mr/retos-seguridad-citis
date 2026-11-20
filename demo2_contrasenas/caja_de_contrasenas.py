"""
DEMO 2: LA CAJA DE CONTRASEÑAS

No necesitas programar. Vas a escribir una contraseña de PRUEBA y, después,
cambiar UN número.

Qué vas a ver
    Parte 1. Tres alumnos guardan su contraseña. Dos tienen la misma. ¿Se nota?
    Parte 2. Tu contraseña de prueba, guardada dos veces con cada método.
    Parte 3. Cuánto tarda tu laptop con cada método.

Dos métodos
    MD5:    rápido y sin sal. Así NO se guardan contraseñas.
    PBKDF2: lento a propósito y con sal (un valor aleatorio distinto para cada alumno).

Cómo correrlo
    Mac:      python3 demo2_contrasenas/caja_de_contrasenas.py
    Windows:  py demo2_contrasenas/caja_de_contrasenas.py
    IDLE:     abre este archivo y presiona F5
"""

# PERILLA: lo único que vas a cambiar en este archivo.
# Es el número de vueltas que da PBKDF2. 600_000 es lo que recomienda OWASP para PBKDF2 con SHA-256.
# Cuando el ponente lo indique, cámbialo por 1_000 y después por 3_000_000.
# Guarda (Ctrl+S o Cmd+S) y vuelve a correr cada vez. Los guiones bajos solo separan los miles.
ITERACIONES = 600_000


# A partir de aquí no necesitas cambiar nada.

import hashlib
import os
import time

ALUMNOS = [
    ("ana", "Cafeteria2026"),
    ("luis", "Torta_de_jamon"),
    ("sofia", "Cafeteria2026"),
]


def con_md5(contrasena):
    return hashlib.md5(contrasena.encode("utf-8")).hexdigest()


def con_pbkdf2(contrasena):
    sal = os.urandom(16)
    huella = hashlib.pbkdf2_hmac("sha256", contrasena.encode("utf-8"), sal, ITERACIONES)
    return sal.hex() + "$" + huella.hex()


def corto(texto):
    return texto[:20] + "..."


def legible(segundos):
    if segundos < 0.001:
        return f"{segundos * 1_000_000:,.2f} microsegundos"
    if segundos < 1:
        return f"{segundos * 1000:,.1f} milisegundos"
    if segundos < 60:
        return f"{segundos:,.1f} segundos"
    if segundos < 3600:
        return f"{segundos / 60:,.1f} minutos"
    if segundos < 86400:
        return f"{segundos / 3600:,.1f} horas"
    return f"{segundos / 86400:,.1f} días"


def medir(funcion, veces):
    inicio = time.perf_counter()
    for _ in range(veces):
        funcion()
    return (time.perf_counter() - inicio) / veces


def main():
    print()
    print("DEMO 2: LA CAJA DE CONTRASEÑAS")
    print(f"PBKDF2 está dando {ITERACIONES:,} vueltas.")

    print()
    print("PARTE 1: tres alumnos guardan su contraseña")
    print(f"  {'Alumno':<8}{'Guardado con MD5':<26}{'Guardado con PBKDF2 y sal':<26}")
    for alumno, contrasena in ALUMNOS:
        print(f"  {alumno:<8}{corto(con_md5(contrasena)):<26}{corto(con_pbkdf2(contrasena)):<26}")
    print("  Pregunta: mirando solo la base de datos, ¿qué dos alumnos tienen la misma contraseña?")
    print("  ¿Con cuál de los dos métodos se nota?")

    print()
    print("PARTE 2: tu contraseña de prueba")
    print("  Nunca escribas una contraseña real en un programa que no conoces. Tampoco en este.")
    try:
        contrasena = input("  Escribe una contraseña de PRUEBA (Enter para usar Cafeteria2026): ")
    except EOFError:
        contrasena = ""
    if contrasena == "":
        contrasena = "Cafeteria2026"
    print("  MD5, vez 1:    ", con_md5(contrasena))
    print("  MD5, vez 2:    ", con_md5(contrasena))
    print("  PBKDF2, vez 1: ", corto(con_pbkdf2(contrasena)))
    print("  PBKDF2, vez 2: ", corto(con_pbkdf2(contrasena)))
    print("  La misma contraseña: con MD5 queda igual; con sal, distinta cada vez.")

    print()
    print("PARTE 3: ¿cuánto tarda tu laptop? (espera unos segundos)")
    sal = os.urandom(16)
    t_md5 = medir(lambda: hashlib.md5(b"Cafeteria2026").hexdigest(), 200_000)
    t_pbkdf2 = medir(lambda: hashlib.pbkdf2_hmac("sha256", b"Cafeteria2026", sal, ITERACIONES), 2)
    print("  Un hash con MD5:     ", legible(t_md5))
    print("  Un hash con PBKDF2:  ", legible(t_pbkdf2))
    print()
    print("  Un millón de hashes con MD5:    ", legible(t_md5 * 1_000_000))
    print("  Un millón de hashes con PBKDF2: ", legible(t_pbkdf2 * 1_000_000))
    print("  (1 segundo = 1,000 milisegundos = 1,000,000 microsegundos)")
    print()
    print("Preguntas para tu pareja")
    print("  1. Alguien se lleva una copia de la base. ¿Por qué te conviene que cada hash tarde tanto?")
    print("  2. Si subes mucho las vueltas, ¿qué le pasa al alumno que solo quiere iniciar sesión?")
    print("     ¿Dónde pondrías el límite?")
    print()


main()
