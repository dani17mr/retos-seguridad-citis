"""
DEMO 3, PARTE A: REGISTROS QUE HABLAN DE MÁS

No necesitas programar. Vas a correr el programa, leer lo que escribe y cambiar UNA palabra.

Este programa simula cuatro inicios de sesión en CafeApp y los anota en un registro (log):
el archivo registro.log, en esta misma carpeta. Al final te muestra lo que quedó escrito.

Cómo correrlo
    Mac:      python3 demo3_secretos/registros.py
    Windows:  py demo3_secretos/registros.py
    IDLE:     abre este archivo y presiona F5
"""

# PERILLA: lo único que vas a cambiar en este archivo.
# Cuando el ponente lo indique, cambia False por True (con T mayúscula),
# guarda el archivo (Ctrl+S o Cmd+S) y vuelve a correrlo.
OCULTAR_SECRETOS = False


# A partir de aquí no necesitas cambiar nada.

from pathlib import Path

ARCHIVO_LOG = Path(__file__).resolve().parent / "registro.log"

INICIOS_DE_SESION = [
    ("10:51:02", "ana", "ana.lopez@escuela.mx", "Cafeteria2026", True),
    ("10:51:40", "luis", "luis.ramos@escuela.mx", "Torta_de_jamon1", False),
    ("10:51:47", "luis", "luis.ramos@escuela.mx", "Torta_de_jamon", True),
    ("10:52:15", "sofia", "sofia.mtz@escuela.mx", "Cafeteria2026", True),
]


def ocultar_correo(correo):
    usuario, _, dominio = correo.partition("@")
    return usuario[:1] + "***@" + dominio


def linea_de_log(hora, usuario, correo, contrasena, exito):
    resultado = "ok" if exito else "fallido"
    if OCULTAR_SECRETOS:
        correo = ocultar_correo(correo)
        contrasena = "****"
    return (f"2026-11-20 {hora} INFO login usuario={usuario} correo={correo} "
            f"password={contrasena} resultado={resultado}")


def main():
    lineas = [linea_de_log(*evento) for evento in INICIOS_DE_SESION]
    ARCHIVO_LOG.write_text("\n".join(lineas) + "\n", encoding="utf-8")

    print()
    print("DEMO 3, PARTE A: REGISTROS QUE HABLAN DE MÁS")
    print("OCULTAR_SECRETOS =", OCULTAR_SECRETOS)
    print("Esto quedó escrito en", ARCHIVO_LOG.name + ":")
    print()
    for linea in lineas:
        print("  " + linea)
    print()
    print("Preguntas para tu pareja")
    if OCULTAR_SECRETOS:
        print("  1. ¿Sigue sirviendo este registro para saber quién entró y cuándo?")
        print("  2. Mejor aún que ocultar la contraseña: ¿hace falta escribirla en el registro?")
    else:
        print("  1. En una empresa, ¿quién podría leer este archivo?")
        print("  2. Mira los dos intentos de luis. ¿Qué revela el intento fallido?")
        print("  Después cambia la PERILLA a True, guarda y vuelve a correr.")
    print()


main()
