class PaymentMethod:
    payment_id: int               # ID único del método de pago
    method_name: str              # Nombre del método de pago (ej., "Tarjeta de Crédito", "PayPal")
    details: dict                 # Detalles específicos del método de pago (ej., {"card_number": "**** **** **** 1234"})

    def __init__(self, payment_id, method_name, details):
        self.payment_id = payment_id
        self.method_name = method_name
        self.details = details
        
    def __str__(self):
        return f'Payment ID: {self.payment_id}, Method Name: {self.method_name}, Details: {self.details}'