class Role:
    role_id: int                  # ID único del rol
    name: str                     # Nombre del rol (ej., "Cliente", "Administrador")
    description: str              # Descripción del rol

    def __init__(self, role_id, name, description):
        self.role_id = role_id
        self.name = name
        self.description = description