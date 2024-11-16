from typing import Any
from models.category import Category


class Product:
    product_id: int               # ID único del producto
    name: str                     # Nombre del producto
    description: str              # Descripción del producto
    price: float                  # Precio unitario
    stock: int                    # Cantidad disponible en inventario
    category: Category            # Categoría del producto
    image_url: str                # URL de la imagen del producto

    def __init__(self, product_id=None, name=None, description=None, price=None, stock=None, category=None, image_url=None):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock
        self.category = category
        self.image_url = image_url
        
    def __str__(self):
        return f' \nID: {self.product_id} \nNombre: {self.name} \nDescripcion: {self.description} \nPrecio: {self.price}, Stock: {self.stock}, Categoria: {self.category}, Imagen URL: {self.image_url}'
    
    def mostrar_detalle(self) -> str:
        """Método concreto en la clase base."""
        return f"ID: {self.product_id} \nNombre: {self.name} \nPrecio: {self.price}"