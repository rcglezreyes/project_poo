from typing import Any
from models.category import Category
from abc import ABC, abstractmethod


class Product(ABC):
    product_id: int               # ID único del producto
    name: str                     # Nombre del producto
    description: str              # Descripción del producto
    price: float                  # Precio unitario
    stock: int                    # Cantidad disponible en inventario
    category: Category            # Categoría del producto
    image_url: str                # URL de la imagen del producto

    def __init__(self, product_id=None, name=None, description=None, price=None, stock=None, category=None, image_url=None):
        self.__product_id = product_id
        self.__name = name
        self.__description = description
        self.__price = price
        self.__stock = stock
        self.__category = category
        self.__image_url = image_url
    
    @property
    def product_id(self) -> int:
        return self.__product_id
    
    @product_id.setter
    def product_id(self, product_id: int) -> None:
        self.__product_id = product_id
    
    @property
    def price(self) -> float:
        return self.__price
    
    @price.setter
    def price(self, price: float) -> None:
        if price < 0:
            raise ValueError('El precio no puede ser negativo.')
        else:
            self.__price = price
    
    
        
    def __str__(self):
        return f' \nID: {self.product_id} \nNombre: {self.name} \nDescripcion: {self.description} \nPrecio: {self.price}, Stock: {self.stock}, Categoria: {self.category}, Imagen URL: {self.image_url}'
    
    def mostrar_detalle(self) -> str:
        """Método concreto en la clase base."""
        return f"ID: {self.product_id} \nNombre: {self.name} \nPrecio: {self.price}"
    
    @abstractmethod
    def calcular_precio(self) -> float:
        """Método abstracto que debe ser implementado por las subclases."""
        pass