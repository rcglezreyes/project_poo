from models.classes_poo.digital_product import DigitalProduct
from models.classes_poo.physical_product import PhysicalProduct
from models.classes_poo.client import Client
from models.classes_poo.administrator import Administrator

class EntityFactory:
    @staticmethod
    def create_entity(type, **kwargs):
        if type == "producto_digital":
            return DigitalProduct(name=kwargs["name"], price=kwargs["price"])
        elif type == "producto_fisico":
            return PhysicalProduct(name=kwargs["name"], price=kwargs["price"])
        elif type == "usuario_cliente":
            return Client(username=kwargs["username"], email=kwargs["email"])
        elif type == "usuario_administrador":
            return Administrator(username=kwargs["username"], email=kwargs["email"])
        else:
            raise ValueError(f"Tipo de entidad no reconocido: {type}")
