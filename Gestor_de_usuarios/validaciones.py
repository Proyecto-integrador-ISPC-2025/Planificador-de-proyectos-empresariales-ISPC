def validar_contrasena(contrasena: str) -> bool:
    """
    Valida que la contraseña cumpla con los requerimientos.
    - Mínimo 6 caracteres.
    - Debe contener al menos una letra y un número.
    """
    if len(contrasena) < 6:
        return False
    
    tiene_letra = any(c.isalpha() for c in contrasena)
    tiene_numero = any(c.isdigit() for c in contrasena)
    
    return tiene_letra and tiene_numero

