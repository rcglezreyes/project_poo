from typing import Protocol

class PaymentProcess(Protocol):
    def startPayment(self, amount: float) -> str:
        """Inicia el proceso de pago."""
        ...

    def verifyPayment(self, reference: str) -> bool:
        """Verifica el estado del pago."""
        ...

    def confirmPayment(self, reference: str) -> str:
        """Confirma que el pago se ha completado."""
        ...
