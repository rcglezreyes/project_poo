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