from models.category import Category


class Product:
    product_id: int               # ID único del producto
    name: str                     # Nombre del producto
    description: str              # Descripción del producto
    price: float                  # Precio unitario
    stock: int                    # Cantidad disponible en inventario
    category: Category            # Categoría del producto
    image_url: str                # URL de la imagen del producto

    def __init__(self, product_id, name, description, price, stock, category, image_url):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock
        self.category = category
        self.image_url = image_url
