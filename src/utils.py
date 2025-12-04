# src/utils.py

def format_result(label, value):
    # Función simplona, pero que Sonar puede marcar por temas de estilo/nombre, etc.
    return f"{label}: {value}"


def do_something_complicated(x, y, z):
    # Función con muchos parámetros y lógica poco clara (potencial smell)
    if x > 10 and y > 5:
        tmp = x * y * z
    else:
        tmp = (x + y) * z

    if tmp > 100:
        return tmp / 3.1416
    return tmp
