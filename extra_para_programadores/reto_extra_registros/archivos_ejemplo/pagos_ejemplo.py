import os

API_KEY = "LLAVE-FALSA-0000"
URL_PAGOS = "https://pagos.ejemplo.mx"


def cobrar(monto):
    secret = os.environ.get("PAGOS_SECRET")
    if secret is None:
        raise RuntimeError("Falta configurar PAGOS_SECRET")
    return {"monto": monto, "estado": "pendiente"}
