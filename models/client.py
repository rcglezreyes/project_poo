from models.payment_method import PaymentMethod
from models.user import User


class Client(User):
    address: str                            # Dirección de envío del cliente
    payment_methods: list[PaymentMethod]    # Lista de métodos de pago asociados al cliente
    preferences: list[str]                  # Lista de preferencias del cliente
    

    def __init__(self, user_id, username, email, password, phone, role, registration_date, address, payment_methods,preferences):
        super().__init__(user_id, username, email, password, phone, role, registration_date)
        self.address = address
        self.payment_methods = payment_methods
        self.preferences = preferences
        
    def __str__(self):
        super_str = super().__str__()
        return f'{super_str} \nAddress: {self.address} \nPayment methods:[{self.payment_methods}] \nPreferences: {self.preferences}'
        