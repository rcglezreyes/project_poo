from models.classes_abstraction_interfaces.payment_process import PaymentProcess

class CardPayment(PaymentProcess):
    def start_payment(self, amount: float) -> str:
        print(f"Iniciando pago con tarjeta por ${amount:.2f}")
        return "ref-tarjeta-123"

    def verify_payment(self, reference: str) -> bool:
        print(f"Verificando pago con referencia {reference}")
        return True

    def confirm_payment(self, reference: str) -> str:
        print(f"Confirmando pago con tarjeta con referencia {reference}")
        return "Pago con tarjeta confirmado"
