"""
RETO 2, NIVEL 3: ¿por qué "lento" es bueno?

Este programa mide cuánto tarda tu laptop en calcular UN hash con MD5 y con PBKDF2.
Tu trabajo es completar los cálculos de abajo y responder la pregunta.

Cómo correrlo:
    Mac:      python3 medir_tiempos.py
    Windows:  py medir_tiempos.py
    IDLE:     abre este archivo y presiona F5

Si ves el error   NameError: name '___' is not defined   es que todavía falta
completar algún ___ de la sección NIVEL 3.
"""

import hashlib
import os
import time

ITERACIONES = 600_000
CONTRASENA = b"Cafeteria2026"


def medir(funcion, veces):
    """Regresa cuántos segundos tarda, en promedio, una llamada a 'funcion'."""
    inicio = time.perf_counter()
    for _ in range(veces):
        funcion()
    return (time.perf_counter() - inicio) / veces


print()
print("Midiendo... (tarda unos segundos)")
sal = os.urandom(16)
segundos_md5 = medir(lambda: hashlib.md5(CONTRASENA).hexdigest(), 200_000)
segundos_pbkdf2 = medir(lambda: hashlib.pbkdf2_hmac("sha256", CONTRASENA, sal, ITERACIONES), 3)

print()
print("Un hash con MD5 tarda    ", f"{segundos_md5 * 1_000_000:.3f}", "microsegundos")
print("Un hash con PBKDF2 tarda ", f"{segundos_pbkdf2 * 1000:.0f}", "milisegundos")
print("(1 segundo = 1,000 milisegundos = 1,000,000 microsegundos)")


# NIVEL 3: completa los cálculos
# Cambia cada ___ por una operación. Usa las variables segundos_md5 y segundos_pbkdf2.

# 1. ¿Cuántos hashes por segundo calcula tu laptop con cada método?
#    Pista: si uno tarda 0.5 segundos, en un segundo caben 1 / 0.5 = 2.
hashes_md5_por_segundo = ___
hashes_pbkdf2_por_segundo = ___

# 2. ¿Cuántas veces más lento es PBKDF2 que MD5?
#    Pista: divide el tiempo de PBKDF2 entre el tiempo de MD5.
veces_mas_lento = ___

# 3. ¿Cuánto tardaría tu laptop en calcular 1 millón de hashes con cada método?
#    Pista: multiplica 1,000,000 por el tiempo de un hash. El resultado queda en segundos.
segundos_millon_md5 = ___
segundos_millon_pbkdf2 = ___


print()
print("Tu laptop calcula", f"{hashes_md5_por_segundo:,.0f}", "hashes por segundo con MD5")
print("Tu laptop calcula", f"{hashes_pbkdf2_por_segundo:,.1f}", "hashes por segundo con PBKDF2")
print("PBKDF2 es", f"{veces_mas_lento:,.0f}", "veces más lento que MD5")
print("Un millón de hashes con MD5:   ", f"{segundos_millon_md5:,.1f}", "segundos")
print("Un millón de hashes con PBKDF2:", f"{segundos_millon_pbkdf2 / 3600:,.1f}", "horas")
print()

# Pregunta para tu pareja (responde en el comentario de abajo):
# Si alguien se lleva la base de datos de CafeApp, ¿por qué te conviene que cada
# intento de adivinar una contraseña le cueste tanto tiempo? ¿Y por qué la sal
# obliga a repetir ese trabajo por cada alumno, en lugar de hacerlo una sola vez?
#
# Respuesta:
