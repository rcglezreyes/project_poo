from models.classes_poo.product import Product

class PhysicalProduct(Product):
    weight: float    # Peso
    height: float    # Alto
    width: float     # Ancho
    depth: float     # Profundidad

    def __init__(self, product_id=None, name=None, description=None, price=None, stock=None, category=None, image_url=None, weight=None, height=None, width=None, depth=None):
        super().__init__(product_id, name, description, price, stock, category, image_url)
        self.__weight = weight
        self.__height = height
        self.__width = width
        self.__depth = depth
        
    @property
    def weight(self) -> float:
        return self.__weight
    
    @weight.setter
    def weight(self, weight: float) -> None:
        self.__weight = weight
        
    @property
    def height(self) -> float:
        return self.__height
    
    @height.setter
    def height(self, height: float) -> None:
        self.__height = height
        
    @property
    def width(self) -> float:
        return self.__width
    
    @width.setter
    def width(self, width: float) -> None:
        self.__width = width
        
    @property
    def depth(self) -> float:
        return self.__depth
    
    @depth.setter
    def depth(self, depth: float) -> None:
        self.__depth = depth
        
    def __str__(self):
        super_str = super().__str__()
        return f'{super_str} \nWeight: {self.weight} \nHeight: {self.height} \nWidth: {self.width} \nDepth: {self.depth}'
    
    def mostrar_detalle(self) -> str:
        """Extiende el método de la clase base con detalles específicos."""
        return f"Producto Fisico: \n{super().mostrar_detalle()} \nPeso: {self.weight}kg \nDimensiones: {self.height}x{self.width}x{self.depth}cm"
    
    def calcular_precio(self) -> float:
        return round(self.price * 1.19, 2)  # Precio base + 10% de impuestos