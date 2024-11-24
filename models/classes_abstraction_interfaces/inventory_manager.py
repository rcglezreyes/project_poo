from abc import ABC, abstractmethod

class InventoryManager(ABC):
    @abstractmethod
    def add_product(self, product, quantity):
        """Añadir un producto al inventario"""
        pass

    @abstractmethod
    def delete_product(self, product):
        """Eliminar un producto del inventario"""
        pass

    @abstractmethod
    def update_stock(self, product, quantity):
        """Actualizar el stock de un producto"""
        pass
