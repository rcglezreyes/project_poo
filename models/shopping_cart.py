from models.client import Client
from models.product import Product


class ShoppingCart:
    cart_id: int                  # ID único del carrito
    client: Client                # Cliente dueño del carrito
    products: list[Product]       # Lista de productos en el carrito
    total: float                  # Total acumulado del carrito

    def __init__(self, cart_id, client, products, total):
        self.cart_id = cart_id
        self.client = client
        self.products = products
        self.total = total