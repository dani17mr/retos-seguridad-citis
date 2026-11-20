# FRAGMENTO A: conexión a la base de datos de CafeApp
# Alicia revisa: ¿lo aprobarías? ¿Por qué?

DB_USUARIO = "cafe_admin"
DB_PASSWORD = "Cafeteria2026!"


def conectar():
    return base_de_datos.conectar(DB_USUARIO, DB_PASSWORD)
