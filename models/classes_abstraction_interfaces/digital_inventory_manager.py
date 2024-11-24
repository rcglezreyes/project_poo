from models.classes_abstraction_interfaces.inventory_manager import InventoryManager

class DigitalInventoryManager(InventoryManager):
    def __init__(self):
        self.inventory = {}

    def add_product(self, product, quantity):
        if product in self.inventory:
            self.inventory[product] += quantity
        else:
            self.inventory[product] = quantity
        print(f"Producto digital añadido: {product} ({quantity})")

    def delete_product(self, product):
        if product in self.inventory:
            del self.inventory[product]
            print(f"Producto digital eliminado: {product}")
        else:
            print(f"Producto {product} no encontrado en el inventario digital.")

    def update_stock(self, product, quantity):
        if product in self.inventory:
            self.inventory[product] = quantity
            print(f"Stock actualizado para {product}: {quantity}")
        else:
            print(f"Producto {product} no encontrado en el inventario digital.")
