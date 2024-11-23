from abc import ABC, abstractmethod

class InventoryManager(ABC):
    @abstractmethod
    def addProduct(self, product, quantity):
        """Añadir un producto al inventario"""
        pass

    @abstractmethod
    def deleteProduct(self, product):
        """Eliminar un producto del inventario"""
        pass

    @abstractmethod
    def updateStock(self, product, quantity):
        """Actualizar el stock de un producto"""
        pass
