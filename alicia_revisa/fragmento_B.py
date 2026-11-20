# FRAGMENTO B: inicio de sesión de CafeApp
# Alicia revisa: ¿lo aprobarías? ¿Por qué?

import logging


def iniciar_sesion(usuario, password):
    logging.info(f"Intento de inicio de sesión: usuario={usuario} password={password}")
    return revisar_credenciales(usuario, password)
