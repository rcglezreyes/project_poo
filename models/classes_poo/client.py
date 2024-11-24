from models.classes_poo.payment_method import PaymentMethod
from models.classes_poo.user import User


class Client(User):
    address: str                            # Dirección de envío del cliente
    payment_methods: list[PaymentMethod]    # Lista de métodos de pago asociados al cliente
    preferences: list[str]                  # Lista de preferencias del cliente
    

    def __init__(self, user_id=None, username=None, email=None, password=None, phone=None, role=None, registration_date=None, address=None, payment_methods=None,preferences=None):
        super().__init__(user_id, username, email, password, phone, role, registration_date)
        self.__address = address
        self.__payment_methods = payment_methods
        self.__preferences = preferences
        
    @property
    def address(self) -> str:
        return self.__address
    
    @address.setter
    def address(self, address: str) -> None:
        self.__address = address
        
    @property
    def payment_methods(self) -> list[PaymentMethod]:
        return self.__payment_methods
    
    @payment_methods.setter
    def payment_methods(self, payment_methods: list[PaymentMethod]) -> None:
        self.__payment_methods = payment_methods
        
    @property
    def preferences(self) -> list[str]:
        return self.__preferences
    
    @preferences.setter
    def preferences(self, preferences: list[str]) -> None:
        self.__preferences = preferences
        
    def __str__(self):
        super_str = super().__str__()
        return f'{super_str} \nAddress: {self.address} \nPayment methods:[{self.payment_methods}] \nPreferences: {self.preferences}'
        