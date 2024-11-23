from models.payment_process import PaymentProcess

class CardPayment(PaymentProcess):
    def startPayment(self, amount: float) -> str:
        print(f"Iniciando pago con tarjeta por ${amount:.2f}")
        return "ref-tarjeta-123"

    def verifyPayment(self, reference: str) -> bool:
        print(f"Verificando pago con referencia {reference}")
        return True

    def confirmPayment(self, reference: str) -> str:
        print(f"Confirmando pago con tarjeta con referencia {reference}")
        return "Pago con tarjeta confirmado"
