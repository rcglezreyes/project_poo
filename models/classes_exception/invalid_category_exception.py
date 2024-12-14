class InvalidCategoryException(Exception):
    """Excepción personalizada para errores en la categoría."""
    def __init__(self, mensaje="Categoría no válida."):
        super().__init__(mensaje)