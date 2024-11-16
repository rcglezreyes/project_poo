from models.product import Product

class PhysicalProduct(Product):
    weight: float    # Peso
    height: float    # Alto
    width: float     # Ancho
    depth: float     # Profundidad

    def __init__(self, product_id, name, description, price, stock, category, image_url, weight, height, width, depth):
        super().__init__(product_id, name, description, price, stock, category, image_url)
        self.weight = weight
        self.height = height
        self.width = width
        self.depth = depth
        
    def __str__(self):
        super_str = super().__str__()
        return f'{super_str} \nWeight: {self.weight} \nHeight: {self.height} \nWidth: {self.width} \nDepth: {self.depth}'
    
    def mostrar_detalle(self) -> str:
        """Extiende el método de la clase base con detalles específicos."""
        return f"Producto Fisico: \n{super().mostrar_detalle()} \nPeso: {self.weight}kg \nDimensiones: {self.height}x{self.width}x{self.depth}cm"
    
    def calcular_precio(self) -> float:
        return round(self.price * 1.19, 2)  # Precio base + 10% de impuestos