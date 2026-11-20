"""
DEMO 1: EL PORTERO DE NOMBRES

No necesitas programar. Vas a escribir nombres y, al final, cambiar UNA palabra.

La regla de CafeApp para nombres de usuario
    1. De 3 a 20 caracteres.
    2. Solo letras sin acento (a-z, A-Z), números (0-9) y guion bajo (_).

El portero revisa cada nombre antes de dejarlo entrar al sistema.
Hoy trabaja con una LISTA DE PROHIBIDOS: rechaza los caracteres que alguien
pensó que eran peligrosos, y deja pasar todo lo demás.

Tu reto
    Escribe nombres que el portero deje pasar, pero que NO cumplan la regla.
    Cada vez que lo logres verás "SE COLÓ". ¿Cuántos logras en 5 minutos?

Cómo correrlo
    Mac:      python3 demo1_portero/portero.py
    Windows:  py demo1_portero/portero.py
    IDLE:     abre este archivo y presiona F5
    Para terminar, presiona Enter sin escribir nada.
"""

# PERILLA: lo único que vas a cambiar en este archivo.
# Cuando el ponente lo indique, cambia False por True (con T mayúscula),
# guarda el archivo (Ctrl+S o Cmd+S) y vuelve a correrlo.
USAR_LISTA_DE_PERMITIDOS = False


# A partir de aquí no necesitas cambiar nada.

PROHIBIDOS = [" ", ".", ",", "!", "?", "@", "#", "/"]
PERMITIDOS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"


def describir(c):
    nombres = {" ": "un espacio", "\t": "un tabulador"}
    return nombres.get(c, '"' + c + '"')


def revisar_largo(nombre):
    if len(nombre) < 3:
        return "tiene menos de 3 caracteres"
    if len(nombre) > 20:
        return "tiene más de 20 caracteres"
    return None


def portero_con_prohibidos(nombre):
    problema = revisar_largo(nombre)
    if problema:
        return False, problema
    for c in nombre:
        if c in PROHIBIDOS:
            return False, "tiene " + describir(c) + ", que está en la lista de prohibidos"
    return True, "no encontró nada de su lista de prohibidos"


def portero_con_permitidos(nombre):
    problema = revisar_largo(nombre)
    if problema:
        return False, problema
    for c in nombre:
        if c not in PERMITIDOS:
            return False, "tiene " + describir(c) + ", que no está en la lista de permitidos"
    return True, "todos sus caracteres están en la lista de permitidos"


def regla_de_cafeapp(nombre):
    problema = revisar_largo(nombre)
    if problema:
        return False, problema
    for c in nombre:
        if c not in PERMITIDOS:
            return False, "tiene " + describir(c) + ", que la regla no permite"
    return True, "cumple las dos condiciones"


def main():
    modo = "LISTA DE PERMITIDOS" if USAR_LISTA_DE_PERMITIDOS else "LISTA DE PROHIBIDOS"
    portero = portero_con_permitidos if USAR_LISTA_DE_PERMITIDOS else portero_con_prohibidos

    print()
    print("DEMO 1: EL PORTERO DE NOMBRES")
    print("El portero trabaja hoy con:", modo)
    if not USAR_LISTA_DE_PERMITIDOS:
        print("Caracteres prohibidos:", "  ".join(describir(c) for c in PROHIBIDOS))
    print("Regla de CafeApp: de 3 a 20 caracteres; solo a-z, A-Z, 0-9 y _")
    print("Reto: escribe nombres que el portero acepte pero que rompan la regla.")

    colados = []
    intentos = 0
    while True:
        print()
        try:
            nombre = input("Escribe un nombre (Enter sin escribir nada para terminar): ")
        except EOFError:
            break
        if nombre == "":
            break
        intentos += 1

        acepta, razon_portero = portero(nombre)
        cumple, razon_regla = regla_de_cafeapp(nombre)
        print("  Portero:          ", "ACEPTADO " if acepta else "RECHAZADO", " (" + razon_portero + ")")
        print("  Regla de CafeApp: ", "CUMPLE   " if cumple else "NO CUMPLE", " (" + razon_regla + ")")
        if acepta and not cumple:
            colados.append(nombre)
            print("  >>> ¡SE COLÓ! El portero dejó pasar un nombre que rompe la regla.")
        print("  Nombres colados hasta ahora:", len(colados))

        if intentos == 3 and not colados and not USAR_LISTA_DE_PERMITIDOS:
            print()
            print("  Pista: mira la lista de prohibidos. ¿Qué caracteres NO están ahí?")
            print("  Piensa en acentos, la ñ, guiones, otros símbolos o emojis.")

    print()
    print("RESUMEN")
    print("  Intentos:", intentos)
    print("  Nombres que se colaron:", len(colados))
    for nombre in colados:
        print("    ", repr(nombre))
    print()
    if USAR_LISTA_DE_PERMITIDOS:
        print("Con la lista de permitidos, ¿lograste colar alguno? Comenta con tu pareja por qué.")
    else:
        print("Ahora cambia la PERILLA de este archivo a True, guarda y vuelve a intentarlo.")
    print()


main()
