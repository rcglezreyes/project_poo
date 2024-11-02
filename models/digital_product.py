from models.product import Product

class DigitalProduct(Product):
    file_url: str    # URL
    format: str      # Formato
    size: float      # Tamano

    def __init__(self, product_id, name, description, price, stock, category, image_url, file_url, format, size):
        super().__init__(product_id, name, description, price, stock, category, image_url)
        self.file_url = file_url
        self.format = format
        self.size = size
        
    def __str__(self):
        super_str = super().__str__()
        return f'{super_str} \nFile URL: {self.file_url} \nFormat: {self.format} \nSize: {self.size}'