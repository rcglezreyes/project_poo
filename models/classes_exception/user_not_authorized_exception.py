class UserNotAuthorizedException(Exception):
    """Se lanza cuando un usuario no autorizado intenta realizar una acción restringida."""
    def __init__(self, mensaje="Usuario no autorizado para realizar esta acción."):
        super().__init__(mensaje)