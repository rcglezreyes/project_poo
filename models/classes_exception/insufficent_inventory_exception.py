class InsufficentInventoryException(Exception):
    """Se lanza cuando no hay suficiente inventario para completar la compra."""
    def __init__(self, mensaje="Inventario insuficiente para el producto solicitado."):
        super().__init__(mensaje)



