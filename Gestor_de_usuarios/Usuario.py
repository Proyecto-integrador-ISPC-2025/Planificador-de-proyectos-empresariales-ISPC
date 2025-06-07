class Usuario:
    """
    Representa a un usuario del sistema con todos sus datos en memoria.
    """
    def init(self, id_usuario: int, nombre_usuario: str, email: str, contrasena_hash: str, rol: str):
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre_usuario
        self.email = email
        self.contrasena_hash = contrasena_hash
        self.rol = rol # 'administrador' o 'estandar'

    def repr(self) -> str:
        """Representación en string del objeto para debugging."""
        return (f"Usuario(id={self.id_usuario}, nombre='{self.nombre_usuario}', rol='{self.rol}')")
