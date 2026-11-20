# FRAGMENTO C: pedidos de un alumno en CafeApp
# Alicia revisa: ¿lo aprobarías? ¿Por qué?


def buscar_pedidos(alumno_id):
    consulta = "SELECT * FROM pedidos WHERE alumno_id = ?"
    return bd.execute(consulta, (alumno_id,))
