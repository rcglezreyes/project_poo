from models.payment_process import PaymentProcess

class PaypalPayment(PaymentProcess):
    def startPayment(self, amount: float) -> str:
        print(f"Iniciando pago con PayPal por ${amount:.2f}")
        return "ref-tarjeta-123"

    def verifyPayment(self, reference: str) -> bool:
        print(f"Verificando pago en PayPal con referencia {reference}")
        return True

    def confirmPayment(self, reference: str) -> str:
        print(f"Confirmando pago en PayPal con referencia {reference}")
        return "Pago con tarjeta confirmado"
