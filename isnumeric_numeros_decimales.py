def es_decimal(cadena):
    """
    Verifica si una cadena representa un número decimal válido.
    """
    try:
        # Intentamos convertir la cadena a un número flotante
        float(cadena)
        return True
    except ValueError:
        # Si ocurre un error, no es un número decimal válido
        return False

# Ejemplos de uso
print(es_decimal("3.14"))  # True
print(es_decimal("42"))    # True
print(es_decimal("-7.5"))  # True
print(es_decimal("abc"))   # False
print(es_decimal("3,14"))  # False (usa coma en lugar de punto)