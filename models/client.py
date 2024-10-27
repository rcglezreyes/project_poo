from models.payment_method import PaymentMethod
from models.user import User


class Client(User):
    address: str                            # Dirección de envío del cliente
    payment_methods: list[PaymentMethod]  # Lista de métodos de pago asociados al cliente

    def __init__(self, user_id, username, email, password, phone, role, registration_date, address, payment_methods):
        super().__init__(user_id, username, email, password, phone, role, registration_date)
        self.address = address
        self.payment_methods = payment_methods