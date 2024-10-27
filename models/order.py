from datetime import datetime
from models.client import Client
from models.payment_method import PaymentMethod
from models.product import Product


class Order:
    order_id: int                  # ID único del pedido
    client: Client                 # Cliente que realiza el pedido
    order_date: datetime           # Fecha en que se realiza el pedido
    products: list[Product]        # Lista de productos incluidos en el pedido
    status: str                    # Estado del pedido (ej., "Confirmado", "Enviado")
    total: float                   # Total del pedido
    payment_method: PaymentMethod  # Método de pago usado
    shipping_address: str          # Dirección de envío

    def __init__(self, order_id, client, order_date, products, status, total, payment_method, shipping_address):
        self.order_id = order_id
        self.client = client
        self.order_date = order_date
        self.products = products
        self.status = status
        self.total = total
        self.payment_method = payment_method
        self.shipping_address = shipping_address
