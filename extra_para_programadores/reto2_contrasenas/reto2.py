"""
RETO 2: GUARDAR CONTRASEÑAS

La historia
    CafeApp guarda las contraseñas de todos los alumnos. Supón que un día alguien
    se lleva una copia de la base de datos. ¿Qué tan fácil sería recuperar las
    contraseñas originales? Depende de CÓMO las guardaste.

Tres ideas que vas a comprobar
    1. Un hash convierte la contraseña en un texto que no se puede regresar al original.
    2. La sal es un valor aleatorio que se mezcla con la contraseña: así, dos personas
       con la misma contraseña quedan guardadas de forma distinta.
    3. Un algoritmo LENTO a propósito (como PBKDF2) hace que probar millones de
       contraseñas sea carísimo para quien robó la base.

Cómo trabajar
    1. Completa el NIVEL 1: cambia cada ___ por el código correcto.
    2. Guarda el archivo.
    3. Corre las pruebas:
           Mac:      python3 probar_reto2.py
           Windows:  py probar_reto2.py
           IDLE:     abre probar_reto2.py y presiona F5
    4. Cuando el Nivel 1 diga "COMPLETO", sigue con el Nivel 2.
       El Nivel 3 está en otro archivo: medir_tiempos.py
"""

import hashlib
import hmac
import os

# Número de vueltas que da PBKDF2. Es la cifra que recomienda OWASP para PBKDF2 con SHA-256.
ITERACIONES = 600_000


# EJEMPLO DE LO QUE NO SE DEBE HACER (ya está escrito; no lo cambies)
def guardar_md5(contrasena):
    """Guarda la contraseña con MD5: rápido, sin sal. Así NO se guardan contraseñas."""
    return hashlib.md5(contrasena.encode("utf-8")).hexdigest()


# NIVEL 1: guardar la contraseña con sal y con un algoritmo lento
# Cambia cada ___ por el código correcto. No cambies nada más.

def guardar_seguro(contrasena):
    """Regresa un texto con el formato  sal$hash  (los dos en hexadecimal)."""

    # Paso 1: genera una sal de 16 bytes aleatorios.
    # Pista: os.urandom(16)
    sal = ___

    # Paso 2: calcula el hash lento con PBKDF2.
    # Pista: hashlib.pbkdf2_hmac("sha256", contrasena.encode("utf-8"), sal, ITERACIONES)
    resultado = ___

    # Paso 3: junta la sal y el hash en un solo texto. Así se guarda en la base de datos.
    return sal.hex() + "$" + resultado.hex()


# NIVEL 2: verificar una contraseña al iniciar sesión
# Cuando alguien inicia sesión, NO se "descifra" lo guardado: se vuelve a calcular el hash
# de lo que escribió, con la MISMA sal, y se compara.
#
# Escribe la función siguiendo estos pasos:
#   Paso 1: separa la sal y el hash.                 Pista: sal_hex, hash_hex = guardado.split("$")
#   Paso 2: convierte la sal de hexadecimal a bytes. Pista: sal = bytes.fromhex(sal_hex)
#   Paso 3: calcula el hash de 'contrasena' con esa sal y las mismas ITERACIONES (igual que en el Nivel 1).
#   Paso 4: compara tu resultado (en hexadecimal) con hash_hex usando hmac.compare_digest(a, b)
#           y regresa lo que te dé (True o False).
#
# Pregunta para tu pareja: ¿por qué el Paso 4 usa hmac.compare_digest y no un simple == ?

def verificar(contrasena, guardado):
    """Regresa True si 'contrasena' es la que se guardó en 'guardado'. Si no, regresa False."""
    raise NotImplementedError("Nivel 2 pendiente")
