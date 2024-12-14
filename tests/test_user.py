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

class TestUserClasses(unittest.TestCase):

    def setUp(self):
        # Configuración de los objetos de prueba
        self.user = User(
            user_id=1,
            username="Carlos",
            email="carlos@example.com",
            password="password123",
            phone="123456789",
            role="cliente",
            registration_date=datetime.now(),
            authorized=True
        )
        
    # Pruebas para la clase User
    def test_user_email_setter_valid(self):
        self.user.email = "new_email@example.com"
        self.assertEqual(self.user.email, "new_email@example.com")

    def test_user_email_setter_invalid(self):
        with self.assertRaises(ValueError):
            self.user.email = "invalid-email"

    def test_user_check_authorization_valid(self):
        self.user.check_authorization()

    def test_user_check_authorization_invalid(self):
        unauthorized_user = User(
            user_id=3,
            username="Pedro",
            email="pedro@example.com",
            password="password123",
            phone="123123123",
            role="cliente",
            registration_date=datetime.now(),
            authorized=False
        )
        with self.assertRaises(UserNotAuthorizedException):
            unauthorized_user.check_authorization()


if __name__ == "__main__":
    unittest.main()
