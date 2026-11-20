"""
RETO 1: VALIDAR ENTRADAS

La historia
    En las tres historias del inicio, el programa confió en lo que escribió el usuario
    y ese dato terminó funcionando como una instrucción. La primera defensa es revisar
    cada dato ANTES de usarlo y aceptar solo lo que esperas.

La regla de CafeApp para los nombres de usuario
    1. Debe tener de 3 a 20 caracteres.
    2. Solo puede usar letras sin acento (a-z, A-Z), números (0-9) y guion bajo (_).

Cómo trabajar
    1. Completa el NIVEL 1: cambia cada ___ por el código correcto.
    2. Guarda el archivo (Ctrl+S en Windows, Cmd+S en Mac).
    3. Corre las pruebas:
           Mac:      python3 probar_reto1.py
           Windows:  py probar_reto1.py
           IDLE:     abre probar_reto1.py y presiona F5
    4. Cuando el Nivel 1 diga "COMPLETO", sigue con el Nivel 2 y después con el Nivel 3.
"""

import ipaddress


# NIVEL 1: completa la función
# Cambia cada ___ por una condición. No cambies nada más.

PERMITIDOS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"


def es_usuario_valido(texto):
    """Regresa True si 'texto' cumple la regla de CafeApp. Si no, regresa False."""

    # Paso 1: revisa el largo.
    # Si tiene menos de 3 caracteres o más de 20, NO es válido.
    # Pista: len(texto) te dice cuántos caracteres tiene el texto.
    if ___:
        return False

    # Paso 2: revisa cada carácter, uno por uno.
    # Si alguno NO está en PERMITIDOS, NO es válido.
    # Pista: la expresión   c not in PERMITIDOS   es True cuando c no está permitido.
    for c in texto:
        if ___:
            return False

    # Si pasó las dos revisiones, es válido.
    return True


# NIVEL 2: piensa como quien quiere romper la regla
# Escribe al menos 3 nombres que DEBEN aceptarse y 3 que DEBEN rechazarse.
# Que sean distintos de los que ya vienen en probar_reto1.py.
# Los nombres van entre comillas y separados por comas, por ejemplo:  "ana_2005",

MIS_VALIDOS = [
    # escribe aquí tus nombres válidos
]

MIS_INVALIDOS = [
    # escribe aquí tus nombres inválidos
]

# Pregunta para discutir con tu pareja (responde en el comentario de abajo):
# Nuestra regla dice qué caracteres SÍ se permiten (lista de permitidos).
# Otra opción sería listar los que NO se permiten (lista de prohibidos).
# ¿Cuál es más segura y por qué?
#
# Respuesta:


# NIVEL 3: validar una dirección IP
# En el Día 1 vimos una función que hacía ping a la IP que escribía el usuario.
# La primera capa de defensa es aceptar solo direcciones IP reales.
#
# Completa es_ip_valida(texto) para que regrese True si el texto es una IP válida
# (IPv4 o IPv6) y False si no lo es.
#
# Pista: ipaddress.ip_address(texto) regresa la IP cuando el texto es válido
#        y lanza un error ValueError cuando no lo es. Usa try / except.

def es_ip_valida(texto):
    """Regresa True si 'texto' es una dirección IP válida. Si no, regresa False."""
    raise NotImplementedError("Nivel 3 pendiente")
