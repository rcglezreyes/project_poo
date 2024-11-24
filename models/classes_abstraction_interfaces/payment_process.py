from typing import Protocol

class PaymentProcess(Protocol):
    def start_payment(self, amount: float) -> str:
        """Inicia el proceso de pago."""
        ...

    def verify_payment(self, reference: str) -> bool:
        """Verifica el estado del pago."""
        ...

    def confirm_payment(self, reference: str) -> str:
        """Confirma que el pago se ha completado."""
        ...
