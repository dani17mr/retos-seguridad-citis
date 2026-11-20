# FRAGMENTO D: búsqueda de alumnos en CafeApp
# Alicia revisa: ¿lo aprobarías? ¿Por qué?


def buscar_alumno(nombre):
    consulta = "SELECT * FROM alumnos WHERE nombre = '" + nombre + "'"
    return bd.execute(consulta)
