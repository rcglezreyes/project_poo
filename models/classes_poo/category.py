class Category:
    category_id: int              # ID único de la categoría
    name: str                     # Nombre de la categoría (ej., "Electrónica", "Ropa")
    type_list: list[str]          # Lista de tipos dentro de la categoría (ej., ["Smartphones", "Laptops"])

    def __init__(self, category_id, name, type_list):
        self.category_id = category_id
        self.name = name
        self.type_list = type_list