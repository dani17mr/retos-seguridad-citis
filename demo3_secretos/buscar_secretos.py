"""
DEMO 3, PARTE B: EL BUSCADOR DE SECRETOS OLVIDADOS

No necesitas programar. Vas a correr el buscador y después editar un archivo de TEXTO.

El buscador revisa los archivos de la carpeta archivos_ejemplo y marca las líneas que
parecen tener un secreto. Su regla: la línea trae una palabra sospechosa
(password, contraseña, token, api_key, secret) Y además un signo = o dos puntos :

Tu reto
    1. Córrelo. Con tu pareja, decide qué líneas marcadas son secretos de verdad
       y cuáles son falsas alarmas.
    2. Abre archivos_ejemplo/notas_equipo.txt con cualquier editor de texto
       (Bloc de notas, TextEdit, VS Code o IDLE). Al final, agrega una línea con un
       secreto FALSO que el buscador NO detecte. Guarda y vuelve a correr.
       ¿Se te escapó?

Cómo correrlo
    Mac:      python3 demo3_secretos/buscar_secretos.py
    Windows:  py demo3_secretos/buscar_secretos.py
    IDLE:     abre este archivo y presiona F5

Si descompones algún archivo de ejemplo, vuelve a descomprimir el zip.
"""

from pathlib import Path

CARPETA = Path(__file__).resolve().parent / "archivos_ejemplo"
PALABRAS_SOSPECHOSAS = ["password", "contraseña", "token", "api_key", "secret"]
LINEAS_ORIGINALES_DE_NOTAS = 5


def es_sospechosa(linea):
    minusculas = linea.lower()
    tiene_palabra = any(palabra in minusculas for palabra in PALABRAS_SOSPECHOSAS)
    tiene_signo = "=" in linea or ":" in linea
    return tiene_palabra and tiene_signo


def main():
    print()
    print("DEMO 3, PARTE B: EL BUSCADOR DE SECRETOS OLVIDADOS")
    print("Regla: una palabra sospechosa (" + ", ".join(PALABRAS_SOSPECHOSAS) + ") Y un = o :")
    print()

    total = 0
    no_detectadas = []
    for archivo in sorted(CARPETA.iterdir()):
        if not archivo.is_file():
            continue
        lineas = archivo.read_text(encoding="utf-8", errors="replace").splitlines()
        for numero, linea in enumerate(lineas, start=1):
            if es_sospechosa(linea):
                total += 1
                print(f"  [MARCADA] {archivo.name}, línea {numero}:  {linea.strip()}")
            elif archivo.name == "notas_equipo.txt" and numero > LINEAS_ORIGINALES_DE_NOTAS and linea.strip():
                no_detectadas.append((numero, linea.strip()))

    print()
    print("Total de líneas marcadas:", total)

    if no_detectadas:
        print()
        print("Líneas que agregaste a notas_equipo.txt y el buscador NO marcó:")
        for numero, linea in no_detectadas:
            print(f"  [NO DETECTADA] línea {numero}:  {linea}")
        print("Si alguna de ellas tiene un secreto, ¡se le escapó al buscador!")

    print()
    print("Preguntas para tu pareja")
    print("  1. De las líneas marcadas, ¿cuáles son secretos de verdad y cuáles son falsas alarmas?")
    print("  2. Hay una línea marcada que no solo es falsa alarma: es la forma correcta de")
    print("     manejar un secreto. ¿Cuál es?")
    if not no_detectadas:
        print("  3. Reto: agrega a notas_equipo.txt un secreto falso que el buscador no detecte.")
    print()


main()
