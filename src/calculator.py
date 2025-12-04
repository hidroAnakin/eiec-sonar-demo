# src/calculator.py

def add(a, b):
    return a + b


def subtract(a, b):
    # Código duplicado a propósito (smell de duplicación)
    result = a - b
    print("Resultado de la resta:", result)  # print innecesario (smell)
    return result


def divide(a, b):
    # Manejo de excepción demasiado genérico (smell)
    try:
        return a / b
    except Exception as e:
        print("Ocurrió un error:", e)
        return None
