from models.inventory_manager import InventoryManager

class PhysicalInventoryManager(InventoryManager):
    def __init__(self):
        self.inventory = {}

    def addProduct(self, product, quantity):
        if product in self.inventory:
            self.inventory[product] += quantity
        else:
            self.inventory[product] = quantity
        print(f"Producto físico añadido: {product} ({quantity})")

    def deleteProduct(self, product):
        if product in self.inventory:
            del self.inventory[product]
            print(f"Producto físico eliminado: {product}")
        else:
            print(f"Producto {product} no encontrado en el inventario físico.")

    # def updateStock(self, product, quantity):
    #     if product in self.inventory:
    #         self.inventory[product] = quantity
    #         print(f"Stock actualizado para {product}: {quantity}")
    #     else:
    #         print(f"Producto {product} no encontrado en el inventario físico.")
