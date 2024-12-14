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

class TestCategoryClasses(unittest.TestCase):

    def setUp(self):
        # Configuración de los objetos de prueba
        self.category = Category(1, "Electrónica", ["Smartphones", "Laptops"])

    # Pruebas para la clase Category
    def test_category_creation(self):
        self.assertEqual(self.category.category_id, 1)
        self.assertEqual(self.category.name, "Electrónica")
        self.assertEqual(self.category.type_list, ["Smartphones", "Laptops"])

if __name__ == "__main__":
    unittest.main()
