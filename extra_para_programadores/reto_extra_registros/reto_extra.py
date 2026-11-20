"""
RETO EXTRA: REGISTROS (LOGS) SIN SECRETOS

La historia
    Cuando algo falla, lo primero que revisa un equipo son los registros (logs).
    Si el programa escribe ahí contraseñas o datos personales, cualquiera que lea los
    logs los ve: soporte, otras herramientas o quien se lleve una copia.
    Y si alguien deja una clave escrita en un archivo, hay que encontrarla antes que otros.

Cómo trabajar
    1. Completa el nivel en el que vas (aquí no hay ___: escribes la función completa).
    2. Guarda el archivo.
    3. Corre las pruebas:
           Mac:      python3 probar_reto_extra.py
           Windows:  py probar_reto_extra.py
           IDLE:     abre probar_reto_extra.py y presiona F5
"""

import re
from pathlib import Path

PALABRAS_SOSPECHOSAS = ["password", "contraseña", "token", "api_key", "secret"]


# NIVEL 1: enmascarar contraseñas en un mensaje de log
#   "login usuario=ana password=Cafe2026"   ->  "login usuario=ana password=****"
#   "usuario=ana contraseña=Cafe2026"       ->  "usuario=ana contraseña=****"
#   "PASSWORD=Secreta1"                     ->  "PASSWORD=****"   (también con mayúsculas)
#   "usuario=ana resultado=ok"              ->  sin cambios
#
# Pista: re.sub(patron, reemplazo, mensaje, flags=re.IGNORECASE)
#   El patrón  (password|contraseña)=\S+  encuentra la palabra, el signo = y todo lo que
#   sigue hasta el siguiente espacio (\S+ significa "uno o más caracteres que no son espacio").
#   En el reemplazo,  \1  vuelve a poner la palabra tal como venía, con sus mayúsculas.
#   Escribe el patrón y el reemplazo con r antes de las comillas:  r"..."

def enmascarar_contrasena(mensaje):
    """Regresa el mensaje con el valor de la contraseña cambiado por ****."""
    raise NotImplementedError("Nivel 1 pendiente")


# NIVEL 2: enmascarar un correo
#   "ana.lopez@escuela.mx"  ->  "a***@escuela.mx"   (primera letra, ***, y el dominio completo)
#   "jo@uni.mx"             ->  "j***@uni.mx"
#   "sin-arroba"            ->  "***"               (si no es un correo, se oculta todo)
#   "@escuela.mx"           ->  "***"               (si no hay nada antes de la @, también)
#
# Pista: usuario, arroba, dominio = correo.partition("@")
#        Si arroba está vacío o usuario está vacío, no es un correo válido.

def enmascarar_correo(correo):
    """Regresa el correo con la parte del usuario oculta."""
    raise NotImplementedError("Nivel 2 pendiente")


# NIVEL 3: buscar secretos olvidados en una carpeta
# Revisa cada archivo de la carpeta y regresa una lista de parejas
# (nombre_del_archivo, numero_de_linea) con las líneas sospechosas.
#
# La regla: una línea es sospechosa si contiene alguna de las PALABRAS_SOSPECHOSAS
# (sin importar mayúsculas) Y además contiene un signo = o dos puntos :
# La primera línea de cada archivo es la número 1. Cuenta cada línea una sola vez.
#
# Pistas:
#   for archivo in sorted(Path(carpeta).iterdir()):           recorre los archivos
#   archivo.name                                               el nombre del archivo
#   texto = archivo.read_text(encoding="utf-8")                lee el archivo completo
#   for numero, linea in enumerate(texto.splitlines(), start=1):   cada línea con su número
#   minusculas = linea.lower()                                 la línea en minúsculas
#   any(palabra in minusculas for palabra in PALABRAS_SOSPECHOSAS)    ¿trae alguna palabra?
#
# Cuando pase, mira los hallazgos con tu pareja: ¿cuáles son secretos de verdad
# y cuáles son falsas alarmas? ¿Cómo mejorarías la regla?

def buscar_secretos(carpeta):
    """Regresa una lista de (nombre_del_archivo, numero_de_linea) sospechosos."""
    raise NotImplementedError("Nivel 3 pendiente")
