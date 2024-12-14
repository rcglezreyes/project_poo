from models.classes_exception.invalid_category_exception import InvalidCategoryException

class Category:
    category_id: int              # ID único de la categoría
    name: str                     # Nombre de la categoría (ej., "Electrónica", "Ropa")
    type_list: list[str]          # Lista de tipos dentro de la categoría (ej., ["Smartphones", "Laptops"])

    def __init__(self, category_id, name, type_list):
        try:
            # Validación de `category_id`
            if not isinstance(category_id, int) or category_id <= 0:
                raise InvalidCategoryException("El category_id debe ser un entero positivo.")
            
            # Validación de `name`
            if not isinstance(name, str) or not name.strip():
                raise InvalidCategoryException("El nombre de la categoría debe ser una cadena no vacía.")
            
            # Validación de `type_list`
            if not isinstance(type_list, list) or not all(isinstance(tipo, str) for tipo in type_list):
                raise InvalidCategoryException("type_list debe ser una lista de cadenas.")
            
            # Asignación de atributos
            self.category_id = category_id
            self.name = name
            self.type_list = type_list

        except InvalidCategoryException as e:
            print(f"Error al crear la categoría: {e}")
            raise

        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")
            raise