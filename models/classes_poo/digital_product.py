from models.classes_poo.product import Product

class DigitalProduct(Product):
    file_url: str    # URL
    format: str      # Formato
    size: float      # Tamano

    def __init__(self, product_id=None, name=None, description=None, price=None, stock=None, category=None, image_url=None, file_url=None, format=None, size=None):
        super().__init__(product_id, name, description, price, stock, category, image_url)
        self.__file_url = file_url
        self.__format = format
        self.__size = size
        
    @property
    def file_url(self) -> str:
        return self.__file_url
    
    @file_url.setter
    def file_url(self, file_url: str) -> None:
        self.__file_url = file_url
        
    @property
    def format(self) -> str:
        return self.__format
    
    @format.setter
    def format(self, format: str) -> None:
        self.__format = format
        
    @property
    def size(self) -> float:
        return self.__size
    
    @size.setter
    def size(self, size: float) -> None:
        self.__size = size
        
    def __str__(self):
        super_str = super().__str__()
        return f'{super_str} \nFile URL: {self.file_url} \nFormat: {self.format} \nSize: {self.size}'
    
    def mostrar_detalle(self) -> str:
        """Extiende el método de la clase base con detalles específicos."""
        return f"Producto Digital: \n{super().mostrar_detalle()} \nURL del archivo: {self.file_url} \nFormato: {self.format} \nTamaño: {self.size}MB"
    
    def calcular_precio(self) -> float:
        return round(self.price * 1.07, 2)