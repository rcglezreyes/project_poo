import unittest
from datetime import datetime
from models.classes_poo.category import Category
from models.classes_poo.product import Product
from models.classes_poo.digital_product import DigitalProduct
from models.classes_poo.user import User
from models.classes_poo.client import Client
from models.classes_poo.shopping_cart import ShoppingCart
from models.classes_exception.insufficent_inventory_exception import InsufficentInventoryException
from models.classes_exception.user_not_authorized_exception import UserNotAuthorizedException

class TestProductClasses(unittest.TestCase):

    def setUp(self):
        # Configuración de los objetos de prueba
        self.category = Category(1, "Electrónica", ["Smartphones", "Laptops"])
        self.product = DigitalProduct(
            product_id=1,
            name="Laptop",
            description="Laptop de alta gama",
            price=1500.00,
            stock=5,
            category=self.category,
            image_url="http://example.com/laptop.jpg",
            file_url="http://example.com/download",
            format="PDF",
            size=2.5
        )

    # Pruebas para la clase Product
    def test_product_price_setter_valid(self):
        self.product.price = 2000.00
        self.assertEqual(self.product.price, 2000.00)

    def test_product_price_setter_invalid(self):
        with self.assertRaises(ValueError):
            self.product.price = -10.00

    def test_product_stock_setter_valid(self):
        self.product.stock = 10
        self.assertEqual(self.product.stock, 10)

    def test_product_stock_setter_invalid(self):
        with self.assertRaises(ValueError):
            self.product.stock = -5

    def test_product_reduce_stock_valid(self):
        self.product.reduce_stock(2)
        self.assertEqual(self.product.stock, 3)

    def test_product_reduce_stock_insufficient(self):
        with self.assertRaises(InsufficentInventoryException):
            self.product.reduce_stock(10)


if __name__ == "__main__":
    unittest.main()
