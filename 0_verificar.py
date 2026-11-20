"""
PASO 0: revisa que tu Python esté listo para el taller.

Cómo correrlo:
    Mac:      python3 0_verificar.py
    Windows:  py 0_verificar.py
    IDLE:     abre este archivo y presiona F5
"""

import sys

print()
print("Revisando tu Python...")
print("  Versión:", sys.version.split()[0])

listo = True

if sys.version_info < (3, 8):
    print("  [FALLA] Necesitas Python 3.8 o superior. Trabaja en pareja con alguien que lo tenga.")
    listo = False
else:
    print("  [OK] La versión sirve para el taller.")

try:
    import hashlib
    hashlib.pbkdf2_hmac("sha256", b"prueba", b"sal", 1000)
    import ipaddress
    import re
    import pathlib
    import hmac
    print("  [OK] Están los módulos que vamos a usar (hashlib, ipaddress, re, pathlib, hmac).")
except Exception as error:
    print("  [FALLA] Falta algo en tu instalación de Python:", error)
    listo = False

print()
if listo:
    print("Todo listo. Levanta la mano o avísale al ponente: ya puedes empezar.")
else:
    print("Algo no está bien. No te preocupes: júntate con la pareja de al lado.")
print()
