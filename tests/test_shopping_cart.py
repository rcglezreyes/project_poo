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

class TestShoppingCartClasses(unittest.TestCase):

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
        self.client = Client(
            user_id=2,
            username="Maria",
            email="maria@example.com",
            password="password123",
            phone="987654321",
            role="cliente",
            registration_date=datetime.now(),
            address="Calle 123",
            payment_methods=[],
            preferences=["Electrónica", "Ropa"]
        )
        self.shopping_cart = ShoppingCart(1, self.client, [], 0.0)

    # Pruebas para la clase ShoppingCart
    def test_shopping_cart_add_product(self):
        self.shopping_cart.agregar_producto(self.product)
        self.assertEqual(len(self.shopping_cart.products), 1)
        self.assertEqual(self.shopping_cart.products[0].name, "Laptop")
            
            
    def test_shopping_cart_add_product_by_name_and_price(self):
        product = DigitalProduct(
            product_id=len(self.shopping_cart.products) + 1,
            name="Mouse",
            description="Mouse óptico",
            price=25.99,
            stock=10,
            category=self.category,
            image_url="http://example.com/mouse.jpg"
        )
        self.shopping_cart.products.append(product)
        self.assertEqual(len(self.shopping_cart.products), 1)
        self.assertEqual(self.shopping_cart.products[0].name, "Mouse")
        self.assertEqual(self.shopping_cart.products[0].price, 25.99)

    def test_shopping_cart_total(self):
        self.shopping_cart.agregar_producto(self.product)
        self.shopping_cart.total += self.product.price
        self.assertEqual(self.shopping_cart.total, 1500.00)


if __name__ == "__main__":
    unittest.main()
