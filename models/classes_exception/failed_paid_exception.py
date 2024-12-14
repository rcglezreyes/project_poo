class FailedPaidException(Exception):
    """Se lanza cuando ocurre un error en el procesamiento del pago."""
    def __init__(self, mensaje="El pago no pudo ser procesado."):
        super().__init__(mensaje)