from models.inventory_manager import InventoryManager

class DigitalInventoryManager(InventoryManager):
    def __init__(self):
        self.inventory = {}

    def addProduct(self, product, quantity):
        if product in self.inventory:
            self.inventory[product] += quantity
        else:
            self.inventory[product] = quantity
        print(f"Producto digital añadido: {product} ({quantity})")

    def deleteProduct(self, product):
        if product in self.inventory:
            del self.inventory[product]
            print(f"Producto digital eliminado: {product}")
        else:
            print(f"Producto {product} no encontrado en el inventario digital.")

    def updateStock(self, product, quantity):
        if product in self.inventory:
            self.inventory[product] = quantity
            print(f"Stock actualizado para {product}: {quantity}")
        else:
            print(f"Producto {product} no encontrado en el inventario digital.")
