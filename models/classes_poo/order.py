from datetime import datetime
from models.classes_poo.client import Client
from models.classes_poo.payment_method import PaymentMethod
from models.classes_poo.product import Product
from models.classes_pattern_observer.subject import Subject
from models.classes_exception.failed_paid_exception import FailedPaidException


class Order(Subject):
    order_id: int                  # ID único del pedido
    client: Client                 # Cliente que realiza el pedido
    order_date: datetime           # Fecha en que se realiza el pedido
    products: list[Product]        # Lista de productos incluidos en el pedido
    status: str                    # Estado del pedido (ej., "Confirmado", "Enviado")
    total: float                   # Total del pedido
    payment_method: PaymentMethod  # Método de pago usado
    shipping_address: str          # Dirección de envío

    def __init__(self, order_id=None, client=None, order_date=None, products=None, status=None, total=None, payment_method=None, shipping_address=None):
        super().__init__()
        self.order_id = order_id
        self.client = client
        self.order_date = order_date
        self.products = products
        self.status = status
        self.total = total
        self.payment_method = payment_method
        self.shipping_address = shipping_address
        
    def change_status(self, nuevo_estado):
        self.status = nuevo_estado
        print(f"Pedido {self.order_id} cambió su estado a {self.status}")
        self.notify_observers(f"Pedido {self.order_id} cambió su estado a {self.status}")
        
    def process_pay(self, product, quantity):
        if self.payment_method.method_name != "tarjeta":
            raise FailedPaidException("El método de pago no es válido. Solo se aceptan tarjetas.")
        product.reduce_stock(quantity)       
        return "Pago procesado exitosamente."
