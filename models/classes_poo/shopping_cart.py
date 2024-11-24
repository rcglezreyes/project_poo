from models.classes_poo.client import Client
from models.classes_poo.product import Product
from functools import singledispatchmethod


class ShoppingCart:
    cart_id: int                  # ID único del carrito
    client: Client                # Cliente dueño del carrito
    products: list[Product]       # Lista de productos en el carrito
    total: float                  # Total acumulado del carrito

    def __init__(self, cart_id, client, products, total):
        self.__cart_id = cart_id
        self.__client = client
        self.__products = products
        self.__total = total
        
    @property
    def cart_id(self):
        return self.__cart_id
    
    @cart_id.setter
    def cart_id(self, value):
        self.__cart_id = value
        
    @property
    def client(self):
        return self.__client
    
    @client.setter
    def client(self, value):
        self.__client = value
    
    @property
    def products(self):
        return self.__products
    
    @products.setter
    def products(self, value):
        self.__products = value
    
    @property
    def total(self):
        return self.__total
    
    @total.setter
    def total(self, value):
        self.__total = value
        
    @singledispatchmethod
    def agregar_producto(self, producto):
        """Método base (default) para agregar productos."""
        raise NotImplementedError("Tipo no soportado para agregarProducto.")

    @agregar_producto.register
    def _(self, producto: Product):
        """Agregar un producto por objeto Producto."""
        self.products.append(producto)
        print(f"Producto '{producto.name}' agregado al carrito.")

    @agregar_producto.register
    def _(self, product_id: int, name: str):
        """Agregar un producto por ID y nombre."""
        producto = Product(product_id, name, 0.0)  
        self.products.append(producto)
        print(f"Producto con ID {product_id} y nombre '{name}' agregado al carrito.")

    @agregar_producto.register
    def _(self, name: str, price: float):
        """Agregar un producto por nombre y precio."""
        producto = Product(len(self.products) + 1, name, price)
        self.products.append(producto)
        print(f"Producto '{name}' con precio {price} agregado al carrito.")